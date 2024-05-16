from case_decorators_providers import register_class


@register_class(name="demo_class", alias="demo")
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"
