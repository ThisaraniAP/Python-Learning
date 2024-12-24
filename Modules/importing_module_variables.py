# Importing and renaming a module
import my_module as mm

# Using the variables from the module
a = mm.person["age"]
print(a)

b = mm.person["name"]
print(b)

print(f"{b.title()} is {a} years old.")