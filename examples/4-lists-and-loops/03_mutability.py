# Mutability (or immutability) is an important factor in Python, but it's not
# the easiest concept to grasp, at least at first.

# A string is immutable.  It can't be changed.  The variable it's assigned to
# can be updated, but then it's a different string.  Consider this:
my_string = 'hello'
print(id(my_string))

my_string = 'world'
print(id(my_string))

# The id() function tells us where in memory an object is stored, and acts as
# a defacto identifier.  This shows that my_string is assigned to two
# different memory locations, or two different objects, in succession.

# A list, on the other hand, *can* be changed
my_list = [1, 2, 3]
print(id(my_list))

my_list[1] = 7
print(id(my_list))

my_list.append(10)
print(id(my_list))

# Note that the my_list variable doesn't get reassigned, like my_string did.
# Reassignment is usually a sign you're *not* mutating a value.

# This can be confusing.  For example:
new_list = my_list
print(id(my_list))
print(id(new_list))

# Before running this next line, what do you think you'll see?
print(new_list)

# And what will this display?
new_list[0] = 50
print(new_list)

# But then, what will this display?
print(my_list)

# Why?
