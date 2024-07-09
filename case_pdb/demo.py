def g():
    return 1


def f():
    breakpoint()
    lst = []
    lst.append(g())
    return lst


res = f()
print(res)
