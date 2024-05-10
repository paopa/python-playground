from dataclasses import dataclass


@dataclass
# @dataclass(frozen=True)
class Demo:
    name: str
    age: int
    city: str


if __name__ == "__main__":
    demo = Demo("John", 25, "New York")
    print(demo)
    print(demo.name)
    print(demo.age)
    print(demo.city)
    print(demo.__annotations__)
    print(demo.__dataclass_fields__)
    print(demo.__dataclass_params__)
    print(demo.__dataclass_params__)

    demo.name = "Alex"  # This will work because dataclass is mutable
    # if we would like to make it immutable then we can use frozen=True
    print(demo.name)
