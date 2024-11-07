# Example of using yield in a generator function
def count_up_to(n):
    """
    A simple generator function that yields numbers from 1 up to n

    Args:
        n (int): The maximum number to count up to

    Yields:
        int: The next number in the sequence
    """
    # Start counting from 1
    current = 1

    # Keep yielding numbers until we reach n
    while current <= n:
        yield current  # Pause here and return the current value
        current += 1  # Increment counter for next iteration


# Example usage:
if __name__ == "__main__":
    # Create a generator object
    counter = count_up_to(5)

    # Iterate through the generated values
    print("Counting up to 5:")
    for number in counter:
        print("First loop")
        print(f"Generated number: {number}")
        break

    for number in counter:
        print("Second loop")
        print(f"Generated number: {number}")

    # Another example showing manual iteration
    print("\nManual iteration example:")
    counter2 = count_up_to(3)
    print(next(counter2))  # Prints 1
    print(next(counter2))  # Prints 2
    print(next(counter2))  # Prints 3
