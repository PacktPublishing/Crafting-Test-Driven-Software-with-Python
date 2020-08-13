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
        cmd, args = cmd.split(maxsplit=1)

        if cmd == "add":
            name, num = args.rsplit(maxsplit=1)
            try:
                self.add(name, num)
            except ValueError as err:
                print(err)
                return
        else:
            raise ValueError(f"Invalid command: {cmd}")

    def save(self):
        print(self._contacts)
        with open("./contacts.json", "w+") as f:
            json.dump({"_contacts": self._contacts}, f)
        
    def load(self):
        with open("./contacts.json") as f:
            self._contacts = [tuple(t) for t in json.load(f)["_contacts"]]

    def add(self, name, phonenum):
        if not isinstance(phonenum, str):
            raise ValueError("A valid phone number is required")

        if not self.PHONE_EXPR.match(phonenum):
            raise ValueError(f"Invalid phone number: {phonenum}")

        self._contacts.append((name, phonenum))
        self.save()


def main():
    raise NotImplementedError()
