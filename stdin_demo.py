import sys


def demo_sys_stdin():
    print("Enter 'q' to exit:")
    for line in sys.stdin:
        if "q" == line.rstrip():
            break
        print(f"Input : {line}")
        print("Enter 'q' to exit:")

    print("Exit")

def demo_input():
    while True:
        line = input("Enter 'q' to exit: ")
        if "q" == line:
            break
        print(f"Input : {line}")
    print("Exit")


if __name__ == "__main__":
    # demo_sys_stdin()
    demo_input()
