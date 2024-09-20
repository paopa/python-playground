class MyClass:
    instances = []

    def __new__(cls, *args, **kwargs):
        print("Creating instance in __new__")
        instance = super(MyClass, cls).__new__(cls)
        cls.instances.append(instance)
        return instance

    def __init__(self, value):
        self.value = value
        print("Creating instance")

    @classmethod
    def create_instance(cls, value):
        return cls(value)

    @classmethod
    def get_instances(cls):
        return cls.instances

    def __str__(self) -> str:
        return str({"value": self.value})
    
    def __repr__(self) -> str:
        return self.__str__()


# Create instances using the class method
instance1 = MyClass.create_instance(10)
instance1 = MyClass.create_instance(20)

# Get the instances
print(MyClass.get_instances())
