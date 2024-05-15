"""
This is  a simple example of importing a package and it will print the package name
and then print the current module name

- Single Initialization:
    - When you import a module or package for the first time, Python loads and initializes it.
    - Subsequent imports of the same module or package do not trigger reinitialization.
      Instead, they return the module object from Python's internal cache
      (the sys.modules dictionary).

- Parent Package Initialization:
    - When you import a submodule (e.g., from package import submodule or import package.submodule),
      Python ensures that the parent package (e.g., package) is initialized first.
    - This initialization happens only once, even if you import the submodule multiple times.


"""

# import case_import_order

# from case_import_order import sub
# import case_import_order.sub

# from case_import_order.sub import mod_a
import case_import_order.sub.mod_a

print("case_import_order/demo.py")
