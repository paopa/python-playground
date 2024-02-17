a = None


def fn():
    global a
    print(a)
    a = 10


if __name__ == "__main__":
    fn()
    print(a)
