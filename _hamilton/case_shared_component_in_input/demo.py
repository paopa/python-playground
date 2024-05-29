from hamilton import driver
import sys


class C:
    def __init__(self, name: str):
        self.hey = "hey"
        self.name = name

    def run(self):
        print(self.hey + " " + self.name)


def A(id: int) -> dict:
    """Constant value 35"""
    return {"number": 35, "id": id}


c = None


def B(A: dict) -> dict:
    """Divide A by 2"""
    c.run()
    return dict(answer=A["number"] / 2, id=A["id"])


class Dummy:
    def __init__(self):
        global c
        c = C("John")
        self.driver = driver.Builder().with_modules(sys.modules[__name__]).build()

    def execute(self, id: int):
        return self.driver.execute([B], inputs={"id": id})


if __name__ == "__main__":
    dummy = Dummy()
    print(dummy.execute(1))
