from typing import Any
from hamilton import driver
import sys


def A(id: int, component: Any) -> int:
    """Constant value 35"""
    print(component)
    return {"number": 35, "id": id}


def B(A: int, component: Any) -> dict:
    """Divide A by 2"""
    print(component)
    return dict(answer=A["number"] / 2, id=A["id"])


class Dummy:
    def __init__(self):
        self.component = "this is a dummy component"
        self.driver = driver.Builder().with_modules(sys.modules[__name__]).build()
        self.driver.display_all_functions("dag.png")

    def execute(self, id: int):
        return self.driver.execute([B], inputs={"id": id, "component": self.component})


if __name__ == "__main__":
    dummy = Dummy()
    result = print(dummy.execute(1))
