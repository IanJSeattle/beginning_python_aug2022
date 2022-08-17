# A tuple (short for "multiple") is like a list, but immutable.  Use
# parentheses to define a tuple, like so:
my_tuple = (1, 2, 3)
print(type(my_tuple))

# Like a list, you can access elements, and loop over it
print(my_tuple[0])
print(my_tuple[-2])

for thing in my_tuple:
    print(thing)

# Unlike a list, you can't modify it once it's been created
my_tuple.append(4)
my_tuple[1] = 17
del my_tuple[0]

# Tuples will start to make more sense once we move on to dictionaries
