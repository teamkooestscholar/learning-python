"""
Creating variables
"""
x = 2
y = "Hello World"
print(x) # 2
print(y) # Hello World

"""
Casting
"""
x = str(5)
y = int(4)
z = float(6)
print(x, y, z) # 5 4 6.0

"""
Get the type
"""
x = 52
y = "Hello World"
print(type(x)) # <class 'int'>
print(type(y)) # <class 'str'>

"""
Single or double quotes
NOTE: 
1. It's recommended to use single quotes, but double quotes are also allowed.
2. If you chose to use double quotes, make sure to use single quotes inside the string, and vice versa.
3. Uniform use of quotes is recommended.
"""
x = "Hello World"
# is the same as
x = 'Hello World'

"""
Case-sensitive
"""
a = 4
A = "Hello World"
# A will not overwrite a