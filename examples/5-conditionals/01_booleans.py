# The boolean data type in Python has one of two values: True or False (note
# that capitalization matters).
true_value = True
print(type(true_value))
false_value = False
print(type(false_value))

# Ok so far as it goes.  But what to do with it?
# The magic is in something called casting.  This is where you convert one
# data type into another.  We did it earlier with ints and strings, using the
# str() function, or the int() function.

# This brings up the idea of "truthiness."  This is how any given value would
# convert to boolean
truthy_values = [
    1,
    'hello',
    5.4,
    [1, 2],
    (4, 5)
]
for value in truthy_values:
    print(f'{value} evaluates as {bool(value)}')

falsey_values = [
    0,
    '',
    [],
    ()
]
for value in falsey_values:
    print(f'{value} evaluates as {bool(value)}')

# Important distinction: = vs ==
# A single equals creates an assignment:
foo = 'hello!'

# A double-equals checks equality:
print(foo == 'hello!')

# The == returns a boolean value, either True or False
