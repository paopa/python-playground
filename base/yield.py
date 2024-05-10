def foo():
    yield 1
    yield 2
    yield 3


for v in foo():
    print(v)


def bar():
    print("before yield")
    yield
    print("after yield")


for v in bar():
    print(v)

if __name__ == '__main__':
    '''
    `yield` is a keyword in Python that is used to return from a function 
    without destroying the states of its local variable and when the function is called, 
    the execution starts from the last yield statement. 
    Any function that contains a yield keyword is termed as generator. Hence, yield is what makes a generator.
    
    the FastAPI framework uses Python's `yield` to control the lifespan events when start/stop the server. 
    '''
    pass
