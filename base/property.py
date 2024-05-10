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


def test_demo():
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


class Tree:
    def __init__(self, breed: str, age: int):
        self.__breed = breed
        self.__age = age

    def __get_breed(self) -> str:
        return self.__breed

    def __get_age(self) -> int:
        return self.__age

    def __set_age(self, age: int):
        if age > 15000 or age < 0:
            raise Exception('the age does not make sense')
        self.__age = age

    def __del_age(self):
        del self.__age

    breed = property(fget=__get_breed)
    age = property(fget=__get_age, fset=__set_age, fdel=__del_age)


def test_tree():
    try:
        tree = Tree('cedar', 150)
        print(f'{tree.breed=}')
        # tree.breed = 'oak' # AttributeError: can't set attribute
        print(f'aa: {tree.age=}')
        tree.age = -100
        print(f'bb: {tree.age=}')
    except Exception as e:
        print(f'error：{str(e)}')
    finally:
        print(f'cc: {tree.age=}')


if __name__ == "__main__":
    # test_demo()
    test_tree()
