import pytest

from fizzbuzz import isfizz, isbuzz

@pytest.mark.parametrize("n,res", [
    (1, False), 
    (3, True), 
    (4, False), 
    (6, True)
])
def test_isfizz(n, res):
    assert isfizz(n) is res


@pytest.fixture(scope="function")
def divisible_by5(n):
    return n % 5 == 0


@pytest.mark.parametrize("n", [
    1, 3, 5, 6, 10    
])
def test_isbuzz(n, divisible_by5):
    assert isbuzz(n) is divisible_by5
