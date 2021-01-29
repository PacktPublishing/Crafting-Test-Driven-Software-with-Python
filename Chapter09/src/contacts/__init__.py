import re
import json


class Application:
    PHONE_EXPR = re.compile('^[+]?[0-9]{3,}$')

    def __init__(self):
        self._clear()

    def _clear(self):
        self._contacts = []

    def run(self, text):
        text = text.strip()
        _, cmd = text.split(maxsplit=1)
        try:
            cmd, args = cmd.split(maxsplit=1)
        except ValueError:
            args = None

        if cmd == "add":
            name, num = args.rsplit(maxsplit=1)
            try:
                self.add(name, num)
            except ValueError as err:
                print(err)
                return
        elif cmd == "del":
            self.delete(args)
        elif cmd == "ls":
            self.printlist()
        else:
            raise ValueError(f"Invalid command: {cmd}")

    def save(self):
        with open("./contacts.json", "w+") as f:
            json.dump({"_contacts": self._contacts}, f)
        
    def load(self):
        with open("./contacts.json") as f:
            self._contacts = [
                tuple(t) for t in json.load(f)["_contacts"]
            ]

    def add(self, name, phonenum):
        if not isinstance(phonenum, str):
            raise ValueError("A valid phone number is required")

        if not self.PHONE_EXPR.match(phonenum):
            raise ValueError(f"Invalid phone number: {phonenum}")

        self._contacts.append((name, phonenum))
        self.save()

    def delete(self, name):
        self._contacts = [
            c for c in self._contacts if c[0] != name
        ]
        self.save()

    def printlist(self):
        for c in self._contacts:
            print(f"{c[0]} {c[1]}")


def main():
    import sys
    a = Application()
    a.load()
    a.run(' '.join(sys.argv))
