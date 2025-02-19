import asyncio
import time
import threading


def blocking_io():
    """
    blocking_io() simulates a blocking I/O operation using time.sleep().
    This function is executed in a separate thread to avoid blocking the main event loop.
    The Global Interpreter Lock (GIL) in Python allows only one thread to execute Python bytecode at a time.
    However, I/O operations can release the GIL, allowing other threads to run.
    """
    print(
        f"[{time.strftime('%X')}] blocking_io() started execution at {threading.current_thread().name}"
    )
    time.sleep(3)
    print(
        f"[{time.strftime('%X')}] blocking_io() finished execution at {threading.current_thread().name}"
    )
    return "read file result"


async def other_coroutine():
    """
    other_coroutine() is an asynchronous function that simulates a non-blocking task.
    It runs concurrently with other tasks in the event loop, yielding control with await asyncio.sleep().
    This allows the event loop to manage multiple tasks efficiently without blocking.
    """
    for i in range(8):
        print(f"[{time.strftime('%X')}] other_coroutine() is running (step {i})")
        await asyncio.sleep(0.5)


async def main():
    """
    main() is the entry point of the asyncio program.
    It demonstrates the use of the event loop to manage concurrent execution of tasks.
    The event loop is responsible for scheduling and running asynchronous tasks.
    Here, run_in_executor() is used to offload the blocking I/O operation to a separate thread.
    This allows the event loop to continue running other coroutines without being blocked.
    """
    loop = asyncio.get_running_loop()
    print(
        f"[{time.strftime('%X')}] main() started at {threading.current_thread().name}"
    )

    # use run_in_executor to move blocking_io to the thread pool
    blocking_task = loop.run_in_executor(None, blocking_io)

    # run another coroutine concurrently
    await other_coroutine()

    # wait for blocking_io to finish and get the result
    result = await blocking_task
    print(f"[{time.strftime('%X')}] result: {result}")


if __name__ == "__main__":
    """
    The asyncio.run() function is used to execute the main() coroutine.
    It sets up the event loop, runs the coroutine, and closes the loop when finished.
    This ensures that all asynchronous tasks are completed before the program exits.
    """
    asyncio.run(main())

    print(f"[{time.strftime('%X')}] end of program")
