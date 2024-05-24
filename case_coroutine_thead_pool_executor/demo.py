import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


async def dummy():
    print("Dummy coroutine")
    await long_running_task()


def long_running_task_sync():
    print("Long running task")
    time.sleep(5)
    print("Long running task done!")
    return 42


async def long_running_task():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, long_running_task_sync)
    return result


async def dummy2():
    print("Dummy2 coroutine")


async def main():
    task_1 = asyncio.create_task(dummy())
    task_2 = asyncio.create_task(dummy2())
    await task_1
    await task_2


asyncio.run(main())
