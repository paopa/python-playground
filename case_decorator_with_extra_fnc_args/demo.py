def dec(fnc):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        return fnc(args[0])

    return wrapper


class A:
    @dec
    def hello(self):
        print("world")


if __name__ == "__main__":
    a = A()

    a.hello(x="x", y="y")
