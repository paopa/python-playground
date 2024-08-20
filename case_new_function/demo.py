class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating a new instance of the class")
        # This is done by calling the __new__ method of the parent class (object) to create the instance
        instance = super().__new__(cls)

        # Perform any additional initialization here
        instance.hello = "Hello, World!"

        return instance

    def __init__(self) -> None:
        # In most cases, you would use the __init__ method for initialization instead.
        # The __init__ method is called after the instance has been created by __new__
        # and allows you to set initial attributes and perform other setup tasks.
        print("Initializing the instance of the class")
        pass


# Create an instance of MyClass
my_object = MyClass()
print(my_object.hello)  # Output: Hello, World!
