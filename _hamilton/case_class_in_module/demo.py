from hamilton import driver
import sys


def A(id: int) -> int:
    """Constant value 35"""
    return {"number": 35, "id": id}


def B(A: int) -> dict:
    """Divide A by 2"""
    return dict(answer=A["number"] / 2, id=A["id"])


class Dummy:
    def __init__(self):
        self.driver = driver.Builder().with_modules(sys.modules[__name__]).build()

    def execute(self, id: int):
        return self.driver.execute([B], inputs={"id": id})


if __name__ == "__main__":
    dummy = Dummy()
    result = print(dummy.execute(1))
