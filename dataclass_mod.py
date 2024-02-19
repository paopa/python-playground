from dataclasses import dataclass

'''
Dataclass is a module that provides a decorator and functions for automatically adding special methods to classes.
It was added to the standard library in Python 3.7. 
Support us easily create the boilerplate code for classes that mostly contain data.
'''


@dataclass
class Tree:
    __breed: str
    __age: int
    __height: float

    def __post_init__(self):
        families = {
            'cedar': 'Pinnacle',
            'oak': 'Faceplate',
            'beech': 'Faceplate',
            'camphor': 'Laureate',
            'maple': 'Sapience',
            'phoebe': 'Laureate'
        }

        self.__family = families.get(self.__breed)


cedar = Tree('cedar', 10, 5.5)
print(cedar.__dict__)

if __name__ == '__main__':
    pass
