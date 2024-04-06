import sys

print("Enter 'q' to exit:")
for line in sys.stdin:
    if "q" == line.rstrip():
        break
    print(f"Input : {line}")
    print("Enter 'q' to exit:")

print("Exit")
