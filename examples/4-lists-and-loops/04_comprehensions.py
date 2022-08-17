# Python has a different way to create a new list, called a comprehension.
# This allows a list to be created in-place.  Consider the following code:

squares = []
for i in range(1,11):
    squares.append(i**2)

print(squares)

# Pretty simple, a list of squares, from 1 to 10.

# A comprehension allows you to do the same work in fewer steps:

squares = [i**2 for i in range(1,11)]
print(squares)

# The various pieces are already familiar.  The square brackets make a list:
squares = [...]

# The for loop is perfectly normal:
for i in range(1,11)

# The weirdest part is knowing that the expression before the for loop is what
# will actually be inserted into the loop.
