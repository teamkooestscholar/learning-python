"""
One line, many values, multiple variables
"""
x, y, z = "Orange", "Banana", "Cherry"
print(x) # Orange
print(y) # Banana
print(z) # Cherry

"""
One line, one value, multiple variables
"""
x = y = z = "Orange"
print(x) # Orange
print(y) # Orange
print(z) # Orange

"""
Unpack a collection
"""
fruits = ["Orange", "Banana", "Cherry"]
x, y, z = fruits
print(x) # Orange
print(y) # Banana
print(z) # Cherry

"""
Unpack a collection with a single value
"""
fruits = ["Orange", "Banana", "Cherry", "Strawberry", "Raspberry"]
x, y, *z = fruits
print(x) # Orange
print(y) # Banana
print(z) # ['Strawberry', 'Raspberry']