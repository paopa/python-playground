import asyncio


async def dummy():
    await asyncio.sleep(1)
    print("Dummy coroutine")
    await asyncio.sleep(1)
    print("Dummy coroutine done!")
    return "dummy"


async def dummy2():
    print("Dummy2 coroutine")
    await asyncio.sleep(3)
    print("Dummy2 coroutine done!")
    return "dummy2"


async def main():
    task_1 = dummy()
    task_2 = dummy2()

    res = await asyncio.gather(task_1, task_2)
    print(res)


asyncio.run(main())
