import sys
from unittest import mock

import contacts


class TestMain:
    def test_main(self, capsys):
        def _stub_load(self):
            self._contacts = [("name", "number")]

        with mock.patch.object(contacts.Application, "load", new=_stub_load):
            with mock.patch.object(sys, "argv", new=["contacts", "ls"]):
                contacts.main()

        out, _ = capsys.readouterr()
        assert out == "name number\n"