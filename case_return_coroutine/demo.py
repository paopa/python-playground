"""
If we run the coroutines directly, it won't return the expected result.
the result will be a coroutine object.

"""


async def dummy():
    print("Dummy coroutine")
    return 422


res = dummy()

print(res)
