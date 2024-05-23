from hamilton.experimental.h_async import AsyncDriver
import my_dataflow

import asyncio


# dr = driver.Builder().with_modules(my_dataflow).build()

dr = AsyncDriver({}, my_dataflow)


async def main():
    task1 = asyncio.create_task(dr.execute(["B"]))
    task2 = asyncio.create_task(dr.execute(["B"]))

    print(await task1)
    print(await task2)


# Run the main coroutine
asyncio.run(main())
