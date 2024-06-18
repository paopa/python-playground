def dec(**extra_args):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(func)
            print(extra_args)
            print(args)
            print(kwargs)
            return func(*args, **kwargs)

        return wrapper

    return decorator


class A:
    @dec(x="x", y="y")
    def hello(self):
        print("world")


if __name__ == "__main__":
    a = A()
    a.hello()
