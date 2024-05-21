import asyncio


def dummy():
    print("this is a dummy function")


# Define the first coroutine
async def say_hello():
    dummy()
    print("Hello,")
    await asyncio.sleep(3)  # Simulate an I/O-bound task
    print("world!")


# Define the second coroutine
async def count_to_five():
    dummy()
    for i in range(1, 6):
        print(i)
        await asyncio.sleep(1)  # Simulate an I/O-bound task


# Main coroutine to run both tasks concurrently
async def main():
    # Create tasks
    task1 = asyncio.create_task(say_hello())
    task2 = asyncio.create_task(count_to_five())

    # Wait for both tasks to complete
    await task1
    await task2


# Run the main coroutine
asyncio.run(main())
