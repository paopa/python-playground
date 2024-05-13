# List to hold all decorated classes
registered_classes = []


def register_class(cls):
    # Add the class to the list of registered classes
    registered_classes.append(cls)
    return cls
