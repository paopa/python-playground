arr = [1, 2, 3]


def my_func(a, b, c):
    print(f'arr: {a}, {b}, {c}')


if __name__ == "__main__":
    my_func(*arr)
