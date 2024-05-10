class Demo:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def __private_method(self):
        self.__value += 1
        print("This is a private method")


if __name__ == "__main__":
    obj = Demo(42)
    print(obj.get_value())
    obj.set_value(43)
    print(obj.get_value())
    obj.__value = 44  # this will create a new variable __value in the object
    # print(obj.__value)
    print(obj._Demo__value)
    obj._Demo__value = 44
    print(obj.get_value())
    print(obj.__dict__)

    # obj.__private_method()
    '''
    Python have a convention to use a single underscore prefix for a variable to indicate that it is private.
    However, this is just a convention and does not actually make the variable private.
    so, we can access the private variable using the _<class_name>__<variable_name> syntax.
    
    in the Python community, it is generally considered bad practice to use this syntax to access private variables.
    and it is better to use the public methods to access and modify the private variables.
    
    we're all adults here, and we can make our own decisions.
    this slogan is often used in the Python community to indicate that Python developers are trusted to make their own decisions.
    '''
