fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5,
}


def make_lemonade(count):
    print(f'Making {count} lemonade')


def out_of_stock():
    print('Out of stock')


# count = fresh_fruit.get('lemon', 0)
# if count:
#     make_lemonade(count)
# else:
#     out_of_stock()

# The walrus operator is a new syntax introduced in Python 3.8.
# It assigns values to variables as part of a larger expression.
# It is denoted by := and is useful in while-loops and if-statements.
if count := fresh_fruit.get('lemon', 0):
    make_lemonade(count)
else:
    out_of_stock()
