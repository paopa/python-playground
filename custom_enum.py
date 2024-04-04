from enum import Enum


class Animal(Enum):
    DOG = {"name": "dog", "value": 1}
    CAT = {"name": "cat", "value": 2}
    BIRD = {"name": "bird", "value": 3}

    def demo(self) -> None:
        print(self.value)


if __name__ == "__main__":
    Animal.DOG.demo()
    Animal.CAT.demo()
    Animal.BIRD.demo()
