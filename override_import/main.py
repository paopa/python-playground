from override_import.dummy import w, z

x = "hello"

y = "world"

w = "world"  # this will override the import from dummy.py

if __name__ == "__main__":
    print(f'x: {x}, y: {y}')
    print(f'z: {z}, w: {w}')
