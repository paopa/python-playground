class Demo:

    def __init__(self):
        print("Demo is initialized.")

    def __call__(self) -> str:
        print("Demo is called.")
        return "hello world"

d = Demo()
res = d()
print(res)