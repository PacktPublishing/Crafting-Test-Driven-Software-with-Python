import pytest


def test_something(random_number_generator):
    a = random_number_generator()
    b = 10
    assert a + b >= 10

