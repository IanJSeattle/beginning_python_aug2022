# Critically, elif is dependent upon the initial if condition.  If you need to
# test things which are dependent upon each other, elif is your friend.
# Otherwise, you may want independent if statements.
make_pizza = True
paid = False
ingredients = ['onion', 'pepper', 'mozarella']
stock = ['onion', 'mozarella', 'sauce', 'sausage']

print('Starting conditions:')
print(f'make_pizza: {make_pizza}')
print(f'paid: {paid}')
print(f'ingredients: {ingredients}')
print(f'stock: {stock}')

# First, check that we have all the ingredients on hand
for ingredient in ingredients:
    if ingredient not in stock:
        make_pizza = False

# Then, independently, check to make sure we've been paid
if not paid:  # if paid is False
    make_pizza = False

if make_pizza:
    print("Ok, we're ready to make your pizza")
else:
    print("Unfortunately, we're not ready to make your pizza just yet")
