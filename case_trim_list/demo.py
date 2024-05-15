# Example usage
list = [1, 2, 3, 4, 5, 6]
del list[3:]

print(list)  # Output: [1, 2, 3]

del list[0]

print(list)  # Output: [ 2, 3]

try:
    x = "Hello"

    del x
    print(x)  # Output: NameError: name 'x' is not defined
except Exception as e:
    print(e)


