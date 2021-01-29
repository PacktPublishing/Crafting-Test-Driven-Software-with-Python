import pytest


def myapp():
    print("MyApp Started")


def test_capsys(capsys):
    myapp()

    out, err = capsys.readouterr()
    
    assert out == "MyApp Started\n"
