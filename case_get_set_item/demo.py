class Key:
    def __init__(self, id):
        self.id = id


class Demo:
    def __init__(self):
        self._cache = {1: 1, 2: 2, 3: 3, "a": "a"}

    def __getitem__(self, key: Key) -> int:
        return self._cache[key.id]

    def __setitem__(self, key: Key, value: object):
        self._cache[key] = value


d = Demo()
print(d[Key(1)])
print(d[Key(2)])
print(d[Key(3)])
print(d[Key("a")])
d[Key(2)] = 4

print(d[Key(2)])
