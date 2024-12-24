# Importing a module and using the dir() function

import my_module as mm
import platform

# platform is one of Python's built-in modules
# The dir() or directory function lists all the function and variable names of the module

x = dir(mm)
print(x, "\n")

a = platform.system()
print(a, "\n")

print(dir(platform))
