class Demo:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

    @property
    def age_x(self):
        return self.__age

    '''
    the property getter method shares the same name as the prefix of the setter method.
    '''
    @age_x.setter
    def age_x(self, age):
        self.__age = age


if __name__ == "__main__":
    demo = Demo("John", 28)
    print(demo.name)
    demo.name = "Alex"
    print(demo.name)

    try:
        del demo.name
        print(demo.name)  # AttributeError: 'Demo' object has no attribute '_Demo__name'
    except AttributeError as e:
        print(e)

    print(demo.age_x)
    demo.age_x = 30
    print(demo.age_x)