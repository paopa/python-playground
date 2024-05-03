"""
This is a simple example of a decorator that adds 1 to the result of the function
It can be used to add additional functionality to a function without changing the function itself

How did it work?
The decorator function add_one returns a new function wrapper that calls the original function and adds 1 to the result.
"""


def add_one(func):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs) + 1

    return wrapper


@add_one
def demo(name, a, b):
    return 1


print(demo("hello", a=1, b=2))
