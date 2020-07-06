from fizzbuzz import isfizz, isbuzz

# Move to parametric tests
def test_isfizz():
    assert isfizz(1) is False
    assert isfizz(3) is True
    assert isfizz(4) is False
    assert isfizz(6) is True


def test_isbuzz():
    assert isbuzz(1) is False
    assert isbuzz(3) is False
    assert isbuzz(5) is True
    assert isbuzz(6) is False
    assert isbuzz(10) is True
