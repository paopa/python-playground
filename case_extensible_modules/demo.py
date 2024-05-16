from case_extensible_modules.base import Base
import importlib
import pkgutil


def import_submodules(package_name):
    package = importlib.import_module(package_name)
    submodules = {}

    print(package.__path__)
    print(package.__name__)

    # Iterate through all the submodules in the package
    for _, name, _ in pkgutil.walk_packages(package.__path__, package.__name__ + "."):
        # Import each submodule
        submodule = importlib.import_module(name)
        submodules[name] = submodule
        print(f"Imported {name}")

    return submodules


if __name__ == "__main__":
    # Replace 'my_package' with your package name
    imported_modules = import_submodules("case_extensible_modules.mods")

    # Use the imported modules
    print(imported_modules)

    # Verify subclasses
    print("Subclasses of Base:", Base.__subclasses__())

    for cls in Base.__subclasses__():
        obj = cls()
        obj.run()
