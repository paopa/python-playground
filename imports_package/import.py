from imports_package.bar import bar, foo

'''
Python global variables are not global

In Python, when you import a module, it runs the module's code and creates a module object, 
which contains all the variables and functions defined in the module. 
When you do from module import variable, you're not getting a reference to the original variable in the module, 
but rather a copy of it.  

In your case, foo is a global variable in the bar module. When you import foo into import.py, 
you're getting a copy of foo at the time of import, which is None.
'''

import imports_package.bar as ib

'''
When you do import module as alias, you're importing the entire module under the alias.
This means that all the variables and functions defined in the module are now accessible as attributes of the alias.

In your case, foo is a global variable in the bar module. When you import bar as ib,
you're not getting a copy of foo, but rather a reference to it.
This means that any changes made to foo in the bar module will be reflected when you access foo through ib.
'''

if __name__ == '__main__':
    bar()
    print(foo)
    print(f'globals fn: {globals()['foo']}')

    ib.bar()
    print(ib.foo)
