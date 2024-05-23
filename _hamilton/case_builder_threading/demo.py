from hamilton import driver

import time
import threading


def A(id: int) -> int:
    """Constant value 35"""
    print(f"A is running {id}")
    time.sleep(2)
    print(f"A is done {id}")
    return {"number": 35, "id": id}


def B(A: int) -> float:
    """Divide A by 2"""
    print(f"B is running {A["id"]}")
    time.sleep(3)
    print(f"B is done {A["id"]}")
    return A["number"] / 2


if __name__ == "__main__":
    import __main__

    dr = driver.Builder().with_modules(__main__).build()

    def task(id):
        result = dr.execute([B], inputs={"id": id})
        print(result)

    threads = []
    start_time = time.time()
    for i in range(5):
        thread = threading.Thread(target=task, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2f} seconds")
