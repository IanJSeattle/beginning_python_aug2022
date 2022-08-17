# If you need to know whether a particular value exists in a list, the "in"
# keyword is useful:
in_stock = ['olives', 'onions', 'mozzarella', 'garlic', 'sauce']

if 'onions' in in_stock:
    print('yes, we have onions!')

# The else clause can be used when you need either one thing or the other to
# happen.
request = input('what ingredient would you like on your pizza? ')

if request in in_stock:
    print(f'yes, we have {request} available!')
else:
    print(f"sorry, we don't have {request}.")

# There's another keyword to use here, which is elif:
normal = ['olives', 'onions', 'mozzarella', 'garlic', 'sauce']
now = ['onions', 'sauce']

request = input('what ingredient would you like on your pizza? ')

if request in now:
    print(f'yes, we have {request} available!')
elif request in normal:
    print(f'sorry, normally we have {request}, but not right now.')
else:
    print(f"sorry, we don't have {request}, and don't usually stock it.")

# Critically, elif is dependent upon the initial if condition.  If you need to
# test things which are dependent upon each other, elif is your friend.
# Otherwise, you may want independent if statements.
make_pizza = True
paid = False
ingredients = ['onion', 'pepper', 'mozarella']
stock = ['onion', 'mozarella', 'sauce', 'sausage']

# First, check that we have all the ingredients on hand
for ingredient in ingredients:
    if ingredient not in stock:
        make_pizza = False

# Then, independently, check to make sure we've been paid
if not paid:
    make_pizza = False

if make_pizza:
    print("Ok, we're ready to make your pizza")
else:
    print("Unfortunately, we're not ready to make your pizza just yet")
