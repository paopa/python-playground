d = {"name": "Zara", "age": 7, "empty": "", "none": None}


if d["empty"]:
    print("empty is True")

if d["empty"] is not None:
    print("empty is not None")

if d["empty"] != "":
    print("empty is not empty")

if d["none"]:
    print("none is True")

if d["none"] is None:
    print("none is None")

if d["none"] is not None:
    print("none is not None")

if "empty" in d:
    print("empty is in d")

if "hello" not in d:
    print("hello is not in d")

if d:
    print("d is True")
