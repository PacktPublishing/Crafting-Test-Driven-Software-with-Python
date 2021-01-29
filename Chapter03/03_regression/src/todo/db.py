import json


class BasicDB:
    def __init__(self, path, _fileopener=open):
        self._path = path
        self._fileopener = _fileopener

    def load(self):
        try:
            with self._fileopener(self._path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save(self, values):
        with self._fileopener(self._path, "w+", encoding="utf-8") as f:
            f.write(json.dumps(values))
