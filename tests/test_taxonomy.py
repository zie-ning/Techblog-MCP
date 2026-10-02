import pytest

from techblog_mcp import taxonomy


def test_category_counts():
    # docs/기획.md: 문제 유형 21개, 도메인 10개
    assert len(taxonomy.problem_type_names()) == 21
    assert len(taxonomy.domain_names()) == 10
    assert len(set(taxonomy.problem_type_names())) == 21
    assert "범용" in taxonomy.domain_names()


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("카프카", "Kafka"),
        ("apache kafka", "Kafka"),
        ("spring-boot", "Spring Boot"),
        ("SpringBoot", "Spring Boot"),
        ("nodejs", "Node.js"),
        ("Rabbit MQ", "RabbitMQ"),
        ("K8S", "Kubernetes"),
        ("RabbitMQ 3.12.14", "RabbitMQ"),  # 끝의 버전 번호
        ("OGG(Oracle GoldenGate)", "Oracle GoldenGate"),  # 괄호 안 이름
        ("Spring Cloud AWS (Listener)", "Spring Cloud AWS"),  # 괄호 설명
        ("k6", "k6"),  # 이름 자체의 숫자는 버전으로 보지 않음
        ("없는기술", None),
    ],
)
def test_normalize_technology(raw, expected):
    assert taxonomy.normalize_technology(raw) == expected


def test_alias_index_has_no_conflicts():
    # 같은 별칭이 두 기술에 걸려 있으면 예외가 난다
    taxonomy._alias_index()


def test_similar_technologies():
    assert "Kafka" in taxonomy.similar_technologies("Kafak")


def test_server_enums_match_taxonomy():
    import typing

    from pipeline.extract import schema
    from techblog_mcp import server

    assert typing.get_args(server.ProblemType) == taxonomy.problem_type_names()
    assert typing.get_args(schema.ProblemType) == taxonomy.problem_type_names()
    assert typing.get_args(server.Domain) == typing.get_args(schema.Domain)


def test_technology_category_and_family():
    assert taxonomy.technology("Kafka").category == "메시지 브로커"
    assert taxonomy.technology("Grafana").category == "관측성"
    # 계열: MSK는 Kafka로 묶이고, 상위 기술이 없으면 자기 자신
    assert taxonomy.technology_family("Amazon MSK") == "Kafka"
    assert taxonomy.technology_family("Kafka") == "Kafka"
    assert taxonomy.technology_family("사전에 없는 기술") == "사전에 없는 기술"


def test_every_technology_has_valid_category_and_parent():
    categories = set(taxonomy.technology_categories())
    names = {t.name for t in taxonomy.technologies()}
    for tech in taxonomy.technologies():
        assert tech.category in categories
        if tech.parent:
            assert tech.parent in names
            assert taxonomy.technology(tech.parent).parent is None


def test_validate_rejects_bad_entries():
    good = taxonomy.Technology("Kafka", (), "메시지 브로커")
    with pytest.raises(ValueError):
        taxonomy._validate((good, taxonomy.Technology("X", (), "없는 종류")))
    with pytest.raises(ValueError):
        taxonomy._validate((good, taxonomy.Technology("X", (), "메시지 브로커", parent="없음")))
    child = taxonomy.Technology("MSK", (), "메시지 브로커", parent="Kafka")
    with pytest.raises(ValueError):
        taxonomy._validate((good, child, taxonomy.Technology("Y", (), "메시지 브로커", "MSK")))
