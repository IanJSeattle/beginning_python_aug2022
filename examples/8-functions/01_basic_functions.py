# A function is a collection of code that can be called by using its name
# followed by parentheses.  A simple function:

def say_hello():
    print('Hello!')

# Running the function:

say_hello()

# You can pass information in to a function via parameters and arguments.
# The words "parameter" and "argument" are practically synonymous, though
# there is a technical difference: a parameter is the variable used in the
# function, while the argument is the data passed to and referenced by the
# parameter.

def say_something(something):
    print(something)

say_something('Hi there')

# In this example, "something" is the parameter, and "Hi there!" is the
# argument.  Honestly, the only people who will care about the difference are
# probably running a test and grading you on persnickety stuff that no one
# cares about in the real world.  I'll try to use the correct words.

# Python has two different kinds of parameters: positional parameters, and
# keyword parameters.  In the following code, "size" and "ingredients" are
# positional, and "extras" is a keyword argument.  Positional parameters can
# also be thought of as required parameters, while keyword parameters have a
# default value, so they don't have to be supplied.

def make_pizza(size, ingredients, extras=None):
    """
    Print out instructions to the kitchen for making a pizza as ordered
    """
    print('Please make the following pizza:')

    dough_ounces = {'small': 6, 'medium': 8, 'large': 12}
    print(f'This is a {size} pizza: use {dough_ounces[size]} oz of dough')

    print('With the following ingredients:')
    for thing in ingredients:
        print(f'* {thing}')

    if extras:
        print('And add the following extras:')
        for thing in extras:
            print(f'* {thing}')

# A positional parameter, since it doesn't include a default, must be
# provided.  A keyword parameter, by definition, includes a default value.
# Positional parameters can also be referred to by name, and keyword arguments
# can be speficied by their position.  The following examples all do the same
# thing:

my_size = 'large'
my_ingredients = ['peppers', 'mushrooms', 'pesto', 'mozarella']
my_extras = ['mozarella']

make_pizza(my_size, my_ingredients, my_extras)

make_pizza(my_size, my_ingredients, extras=my_extras)

make_pizza(size=my_size, ingredients=my_ingredients, extras=my_extras)

make_pizza(ingredients=my_ingredients, extras=my_extras, size=my_size)

# Frequently, you'll want to have your function return a value, rather than
# performing some action.  For this, we use the return keyword.

def add(a, b):
    """ Add two numbers together, returning the resulting value. """
    return a + b

print(add(5, 4))
print(add(10.5, 11.2))

# Note that the return keyword ends the function, even if there's more code
# left, so it will frequently be used in if statements to end a function
# early.
