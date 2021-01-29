from unittest import mock

import pytest

from contacts import Application

def test_application():
    app = Application()

    assert app._contacts == []
    assert hasattr(app, "run")


def test_clear():
    app = Application()
    app._contacts == [("NAME", "NUM")]

    app._clear()

    assert app._contacts == []


class TestRun:
    def test_add(self):
        app = Application()

        with mock.patch.object(app, "add") as mockadd:
            app.run("cmd add NAME 333")

        mockadd.assert_called_with("NAME", "333")

    def test_add_surname(self):
        app = Application()

        with mock.patch.object(app, "add") as mockadd:
            app.run("cmd add NAME SURNAME    333   ")

        mockadd.assert_called_with("NAME SURNAME", "333")

    def test_empty(self):
        app = Application()

        with pytest.raises(ValueError):
            app.run("")

    def test_nocmd(self):
        app = Application()

        with pytest.raises(ValueError):
            app.run("nocmd")

    def test_invalid(self):
        app = Application()

        with pytest.raises(ValueError):
            app.run("contacts invalid")

