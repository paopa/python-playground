# List to hold all decorated classes
registered_classes = []


def register_class(cls):
    # Add the class to the list of registered classes
    registered_classes.append(cls)
    return cls


@register_class
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


import os


def create_instance():
    # Fetch the class name from an environment variable
    class_name = os.getenv("CLASS_NAME")

    # Find the class in the registered classes list
    for cls in registered_classes:
        if cls.__name__ == class_name:
            return cls("World")  # Assume the constructor takes one argument

    raise ValueError("Class not found")


# This would typically be set outside of the script, e.g., in the shell
os.environ["CLASS_NAME"] = "MyClass"

instance = create_instance()
print(instance.greet())  # Output should be "Hello, World!"
