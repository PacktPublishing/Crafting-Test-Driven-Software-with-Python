import pytest

import fizzbuzz
from fizzbuzz import outfizz, outbuzz, endnum


@pytest.fixture(params=["fizz", "buzz"])
def expected_output(request):
    text = request.param
    if request.config.getoption("--upper"):
        text = text.upper()
    
    textcasemarker = request.node.get_closest_marker("textcase")
    if textcasemarker:
        textcase, = textcasemarker.args
        if textcase == "upper":
            text = text.upper()
        elif textcase == "lower":
            text = text.lower()
        else:
            raise ValueError("Invalid Test Marker")
    
    yield getattr(fizzbuzz, "out{}".format(request.param)), text


def test_output(expected_output, capsys):
    func, expected = expected_output

    func()

    out, _ = capsys.readouterr()
    assert out == expected


@pytest.mark.textcase("lower")
def test_lowercase_output(expected_output, capsys):
    func, expected = expected_output

    func()

    out, _ = capsys.readouterr()
    assert out == expected


class TestEndNum:
    def test_plainnum(self, capsys):
        endnum(1)
        endnum(4)
        endnum(7)

        out, _ = capsys.readouterr()
        assert out == "1\n4\n7\n"

    def test_omitnum(self, capsys):
        endnum(3)
        endnum(5)
        endnum(15)

        out, _ = capsys.readouterr()
        assert out == "\n\n\n"
