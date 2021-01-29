import re
import json


class Application:
    """Manages a contact book serving the provided commands.

    The contact book itself is saved in a contacts.json file
    in the same directory where the application is started
    and it's loaded back on every new run.

    A contact is composed by any name followed by a valid
    phone number.
    """
    PHONE_EXPR = re.compile('^[+]?[0-9]{3,}$')

    def __init__(self):
        self._clear()

    def _clear(self):
        self._contacts = []

    def run(self, text):
        """Run a provided command.

        :param str text: The string containing the command to run.

        Takes the command to run as a string as it would
        come from the shell, parses it and runs it.

        Each command can support zero or multiple arguments
        separate by an empty space.

        Currently supported commands are:

         - add
         - del
         - ls
        """
        text = text.strip()
        _, cmd = text.split(maxsplit=1)
        try:
            cmd, args = cmd.split(maxsplit=1)
        except ValueError:
            args = None

        if cmd == "add":        
            try:
                name, num = args.rsplit(maxsplit=1)
            except ValueError:
                print("A contact must provide a name and phone number")
                return
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
    raise NotImplementedError()
