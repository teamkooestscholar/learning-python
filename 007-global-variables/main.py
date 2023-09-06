"""
Global variables
"""
# A variable outside of a function, and use it inside the function
x = "awesome"  # This is a global variable

def my_func():
    print("Python is " + x)

my_func() # Python is awesome

# Create a variable with the same name inside a function, this variable will be local, and can only be used inside the function
def my_func():
    x = "fantastic"
    print("Python is " + x)

my_func() # Python is fantastic

print("Python is " + x) # Python is awesome

"""
The `global` keyword
NOTE:
1. If you use the `global` keyword, the variable belongs to the global scope, and can be accessed by any function
2. You can use the `global` keyword if you want to change a global variable inside a function
"""
def my_func():
    global x
    x = "fantastic"
    print("Python is " + x)

my_func() # Python is fantastic

print("Python is " + x) # Python is fantastic