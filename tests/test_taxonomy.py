import pytest

from techblog_mcp import taxonomy


def test_category_counts():
    # docs/기획.md: 문제 유형 20개, 도메인 10개
    assert len(taxonomy.problem_type_names()) == 20
    assert len(taxonomy.domain_names()) == 10
    assert len(set(taxonomy.problem_type_names())) == 20
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
