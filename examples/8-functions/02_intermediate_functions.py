# Python allows you to pass an arbitrary number of arguments to a function, so
# you don't have to specify each one in the code.  This can be handy when you
# can't know exactly what your inputs will be.

def make_pizza(*toppings):
    print('Make a pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')

make_pizza('onions')

make_pizza('mozarella', 'sauce', 'basil', 'garlic')

# Note that the parameter with the asterisk is converted into a tuple, so the
# toppings parameter can do anything a tuple can do, such as be interated
# over.  It also has the limitations of a tuple, so it can't be modified.

# This parameter is frequently called *args, though it can be any name.  The
# companion to *args is **kwargs, which will gather any keyword args into a
# dict.

def make_pizza(*toppings, **special_instructions):
    print('Make a pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')

    if not special_instructions:
        return

    print('Special instructions:')
    for key, value in special_instructions.items():
        print(f'{key}: {value}')

make_pizza('onion', 'basil', 'peppers', sauce='pesto', bake='extra crispy')

make_pizza('cheddar', 'meatballs', sauce='red', delivery='10 pm')

make_pizza('mozarella', 'sauce', 'basil', 'garlic')
