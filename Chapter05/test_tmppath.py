import pytest


def test_tmp(tmp_path):
    f = tmp_path / "file.txt"
    print("FILE: ", f)

    f.write_text("Hello World")

    fread = tmp_path / "file.txt"
    assert fread.read_text() == "Hello World"
