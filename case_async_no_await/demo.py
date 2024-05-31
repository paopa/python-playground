async def demo(id: int):
    print(f"id: {id}")
    s = 0

    for i in range(10):
        _helper(i)
        s += i

    return s


def _helper(i: int):
    print(i)


import asyncio

x = asyncio.run(demo(1))
print(x)

y = asyncio.run(demo(2))
print(y)
