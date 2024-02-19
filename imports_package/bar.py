foo = 10


def bar():
    global foo
    print(f'{foo} in the bar fn')
    foo = 42
    print(f'{foo} in the bar fn')
