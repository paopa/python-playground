d = {"c": 2}


d["b"] = d.pop("a", 0)
d["d"] = d.pop("c", 0)


print(d) # {'b': 0, 'd': 2}

