class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self):
        return str(hash(self))


person = Person("Alice", 25)
print(person)  # Person(name=Alice, age=25)
print(repr(person))  # a unique number in this case

# What is the difference between __str__ and __repr__?
# __str__ is called by str() and print() to get a string representation of the object.
# the __str__ method should return a human-readable string that describes the object.
# This is useful for displaying information to the user.

# __repr__ is called by repr() to get a string representation of the object.
# the __repr__ method should return an unambiguous string representation of the object.
# This is useful for debugging and logging.
