import pytest


def test_something():
    a = 5
    b = 10
    assert a + b == 11


class TestMultiple:
    def test_first(self):
        assert 5 == 5

    def test_second(self):
        assert 10 == 10

