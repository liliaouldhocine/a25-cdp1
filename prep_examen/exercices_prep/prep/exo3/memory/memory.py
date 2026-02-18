class Memory:
    def __init__(self):
        self._data = {}

    def store(self, name, value):
        self._data[name] = value

    def read(self, name):
        return self._data.get(name)

    def clear(self, name):
        if name in self._data:
            del self._data[name]
