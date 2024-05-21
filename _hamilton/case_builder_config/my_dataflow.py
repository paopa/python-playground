from hamilton.function_modifiers import config


def A() -> int:
    """Constant value 35"""
    return 35


@config.when_not(version="remote")
def B__default(A: int) -> float:
    """Divide A by 3"""
    return A / 3


@config.when(version="remote")
def B__remote(A: int) -> float:
    """Divide A by 2"""
    return A / 2
