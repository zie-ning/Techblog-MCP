import techblog_mcp


def test_package_importable():
    # 셋업 확인용: 패키지와 파이프라인 모듈을 불러올 수 있어야 한다
    import pipeline.collect  # noqa: F401

    assert techblog_mcp.__version__ == "0.1.0"
