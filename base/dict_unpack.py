params = {'a': 1, 'b': 2}


def my_func(a, b):
    print(f'params: {a}, {b}')


if __name__ == "__main__":
    my_func(**params)
