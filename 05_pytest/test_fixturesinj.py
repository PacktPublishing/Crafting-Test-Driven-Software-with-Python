import pytest


def test_something(random_number_generator):
    a = random_number_generator()
    b = 10
    assert a + b == 11


@pytest.fixture
def random_number_generator():
    def _number_provider():
        return 1
    yield _number_provider
