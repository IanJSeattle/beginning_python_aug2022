# A list is a complex data type that can hold multiple values of any type
my_list = ['a', 1, 'hello']

# Each element in a list is accessed by its index number, starting at zero:
#
# my_list now contains:
# 0: 'a'
# 1: 1
# 2: 'hello'
print(my_list[0])
print(my_list[1])
print(my_list[2])

# An element can be modified without changing the rest of the list
# Note that this makes lists "mutable" (they can be changed)
my_list[1] = 'hearty'
print(my_list)

# Add elements to a list using the .append() method
my_list.append('was said')
print(my_list)

# Remove elements from a list using the del keyword
del my_list[1]
print(my_list)

# Accessing the end of the list
print(my_list[-1])
