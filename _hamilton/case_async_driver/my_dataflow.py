import time
import asyncio


async def A() -> int:
    """Constant value 35"""
    print("A is running")
    await asyncio.sleep(2)
    print("A is done")
    return 35


async def B(A: int) -> float:
    """Divide A by 2"""
    print("B is running")
    await asyncio.sleep(5)
    print("B is done")
    return A / 2
