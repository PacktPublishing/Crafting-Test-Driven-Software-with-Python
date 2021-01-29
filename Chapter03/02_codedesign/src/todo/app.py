import functools


class TODOApp:
    def __init__(self, 
                 io=(input, functools.partial(print, end="")), 
                 dbmanager=None):
        self._in, self._out = io
        self._quit = False
        self._entries = []
        self._dbmanager = dbmanager

    def run(self):
        if self._dbmanager is not None:
            self._entries = self._dbmanager.load()

        self._quit = False
        while not self._quit:
            self._out(self.prompt(self.items_list()))
            command = self._in()
            self._dispatch(command)

        if self._dbmanager is not None:
            self._dbmanager.save(self._entries)
        
        self._out("bye!\n")

    def prompt(self, output):
        return """TODOs:
{}

> """.format(output)

    def items_list(self):
        enumerated_items = enumerate(self._entries, start=1)
        return "\n".join(
            "{}. {}".format(idx, entry) for idx, entry in enumerated_items
        )

    def _dispatch(self, cmd):
        cmd, *args = cmd.split(" ", 1)
        executor = getattr(self, "cmd_{}".format(cmd), None)
        if executor is None:
            self._out("Invalid command: {}\n".format(cmd))
            return
        
        executor(*args)

    def cmd_quit(self, *_):
        self._quit = True

    def cmd_add(self, what):
        self._entries.append(what)

    def cmd_del(self, idx):
        idx = int(idx) - 1  # regression?
        if idx < 0 or idx >= len(self._entries):
            self._out("Invalid index\n")
            return

        self._entries.pop(idx)
        
