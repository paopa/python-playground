import os
from case_decorators_providers import registered_classes


def create_instance():
    # Fetch the class name from an environment variable
    class_name = os.getenv("CLASS_NAME")

    # Find the class in the registered classes list
    return registered_classes.get(class_name)(name="World")

    # for cls in registered_classes:
    #     if cls.__name__ == class_name:
    #         return cls("World")  # Assume the constructor takes one argument
    # raise ValueError("Class not found")


# This would typically be set outside of the script, e.g., in the shell
os.environ["CLASS_NAME"] = "demo_class"

instance = create_instance()
print(instance.greet())  # Output should be "Hello, World!"
