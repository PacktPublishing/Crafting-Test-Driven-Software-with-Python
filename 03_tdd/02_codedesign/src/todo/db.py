import shelve


class ShelveLoader:
    def load(self, path):
        db = shelve.open(path)
        try:
            return db["entries"]
        except KeyError:
            return []

    def save(self, path, entries):
        pass
        