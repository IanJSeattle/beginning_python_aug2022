# Python files are technically called modules.  A module can be imported into
# a different module, and the code present in it can be run in that different
# module.  This makes code reuse very straightforward.

# In this module, I'll define a couple useful (well, "useful") functions, and
# then in the next module, import them and use them.

def say_hello():
    """ Print a simple message """
    print('hello!')


def say_something(thing):
    """ Print the specified message """
    print(thing)


def say_thing_lots(thing, times):
    """ Print the specified message multiple times """
    for _ in range(times):
        print(thing)


def make_pizza(*toppings, **instructions):
    """ Print out pizza-making instructions """
    print('Please make the following pizza:')
    for topping in toppings:
        print(f'* {topping}')

    if not instructions:
        return

    print('With the following special instructions:')
    for key, value in instructions.items():
        print(f'{key}: {value}')

def say_name():
    """ print out the current module's name """
    print(f'__name__ is currently {__name__}')

say_name()
