"""
Output variables
"""
x = "Hello World"
print(x) # Hello World

x = "Hello World"
print("x") # x

x = "Hello World"
print(x) # Hello World

"""
The "+" operator
"""
# With spaces
x = "Python "
y = "is "
z = "awesome"
print(x + y + z) # Python is awesome

x = "Python"
y = "is"
z = "awesome"
print(x + " " + y +  " " + z) # Python is awesome

# Without spaces
x = "Python"
y = "is"
z = "awesome"
print(x + y  + z) # Pythonisawesome

"""
For numbers
"""
#  Good example
x = 10
y = 20
print(x + y) # 30

# Bad example
x = 10
y = "20"
print(x + y) # TypeError: unsupported operand type(s) for +: 'int' and 'str'