from fizzbuzz import outfizz, outbuzz, endnum


def test_outfizz(capsys):
    outfizz()

    out, _ = capsys.readouterr()
    assert out == "fizz"


def test_outbuzz(capsys):
    outbuzz()

    out, _ = capsys.readouterr()
    assert out == "buzz"


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
