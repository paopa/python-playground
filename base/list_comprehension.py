origin = [1, 2, 3, 4, 5]

# this is the traditional way to copy a list
tmp = []

for x in origin:
    tmp.append(x)

print(tmp)

# this is the list comprehension way to copy a list
foo = [x for x in origin]

print(foo)

# this is the list comprehension way to copy a list and modify it
bar = [x * 2 for x in origin]

print(bar)

# this is the list comprehension way to copy a list and filter it
baz = [x for x in origin if x % 2 == 0]

print(baz)

if __name__ == '__main__':
    pass
