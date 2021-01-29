import os
import json

from contacts import Application


class TestLoading:
    def test_load(self):
        app = Application()

        with open("./contacts.json", "w+") as f:
            json.dump({"_contacts": [("NAME SURNAME", "3333")]}, f)
        
        app.load()

        assert app._contacts == [
            ("NAME SURNAME", "3333")
        ]


class TestSaving:
    def test_save(self):
        app = Application()
        app._contacts = [
            ("NAME SURNAME", "3333")
        ]

        try:
            os.unlink("./contacts.json")
        except FileNotFoundError:
            pass

        app.save()
        
        with open("./contacts.json") as f:
            assert json.load(f) == {"_contacts": [["NAME SURNAME", "3333"]]}
