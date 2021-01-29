
class FakeServer:
    def __init__(self):
        self.last_command = None
        self.messages = []

    def __call__(self, *args, **kwargs):
        return self

    def send(self, data):
        callid, command, args, kwargs = data
        self.last_command = command
        self.last_args = args

    def recv(self, *args, **kwargs):
        if self.last_command == "dummy":
            return "#RETURN", None
        elif self.last_command == "create":
            return "#RETURN", ("fakeid", tuple())
        elif self.last_command == "append":
            self.messages.append(self.last_args[0])
            return "#RETURN", None
        elif self.last_command == "__getitem__":
            return "#RETURN", self.messages[self.last_args[0]]
        elif self.last_command == "__len__":
            return "#RETURN", len(self.messages)
        elif self.last_command in ("incref", "decref", "accept_connection"):
            return "#RETURN", None
        else:
            return "#ERROR", ValueError("%s - %r" % (self.last_command, self.last_args))

    def close(self):
        pass
