# my_dataflow.py
def A() -> int:
    """Constant value 35"""
    return 35


def B(A: int) -> float:
    """Divide A by 3"""
    return A / 3


def C(A: int, B: float) -> float:
    """Square A and multiply by B"""
    return A**2 * B
