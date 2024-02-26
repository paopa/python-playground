class Tree:
    """
    This is a simple class to demonstrate how to use the `*` operator in a class
    definition. The `*` operator is used to indicate that the arguments are keyword
    only arguments. This means that the arguments must be passed as keyword arguments
    when the class is instantiated. This is a new feature in Python 3.8.
    """

    def __init__(self, *, left, right):
        self.left = left
        self.right = right


if __name__ == "__main__":
    tree = Tree(left="left", right="right")
    print(tree.left)
    print(tree.right)
