# List to hold all decorated classes
registered_classes = {}


def register_class(name: str, alias: str = None):
    def wrapper(cls):
        print(alias)
        registered_classes[name] = cls
        return cls

    return wrapper
