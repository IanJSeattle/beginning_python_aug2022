""" this module contains the interface for a pizza restaurant cashier.  it asks
what the customer is trying to order, and prints that order out in the kitchen.

we assume that the print() statement will go to the appropriate place.
we assume that everyone involved is a genius and will never make a mistake. """

class Pizza:
    sizes = ['small', 'medium', 'large', 'gigantic']
    size = ''
    toppings = None
    num_slices = 0

    def __init__(self, size=''):
        self.size = size

    def __repr__(self):
        return f"Pizza('{self.size}')"

    def __str__(self):
        return f"A {self.size} pizza"


def show_menu(items):
    """ print out a menu of items, itemized by number """
    for num, item in enumerate(items):
        print(f'{num+1}: {item}')


def get_toppings(toppings):
    """ ask for toppings.  expect a list of numbers, like: 2 4 5 """
    toppings = toppings['in stock']
    show_menu(toppings)
    valid_answers = []
    while True:
        response = input('Which toppings? ')
        responses = response.split()
        for num in responses:
            if num.isdigit() and int(num) >= 1 and int(num) <= len(toppings):
                valid_answers.append(num)
        if len(valid_answers) == len(responses):
            break  # valid answers recorded, exit loop
    # codify our response into a list of toppings and return it
    requested_toppings = []
    for answer in valid_answers:
        requested_toppings.append(toppings[int(answer)-1])
    return requested_toppings


def get_size(pizza_sizes):
    show_menu(pizza_sizes)
    size = ''
    while not size.isdigit() or int(size) < 1 or int(size) > len(pizza_sizes):
        size = input('Which size? ')
    return pizza_sizes[int(size)-1]


def get_order(toppings, name='Anonymouse'):
    """ get the order from the customer """
    pizza = Pizza()
    cust_name = input('Customer name: ')
    if not cust_name:
        cust_name = name
    size = get_size(pizza.sizes)
    print(size)
    requested_toppings = get_toppings(toppings)
    print(requested_toppings)
    pizza.toppings = requested_toppings
    pizza.size = size
    return pizza, cust_name


def send_to_kitchen(pizza, name):
    """ print out the new order for the kitchen to make """
    print(f'dear kitchen, please make this pizza for {name}:')
    print(f'Size: {pizza.size}')
    print(f'Toppings:')
    for item in pizza.toppings:
        print(f'\t- {item}')


def main():
    toppings = {
        'standard':
            [
                'cheese',
                'peppers',
                'onions',
                'mushroom',
                'pepperoni',
                'sausage',
                'broccoli'
            ],
        'in stock':
            [
                'cheese',
                'onions',
                'pepperoni',
                'broccoli'
            ]
    }
    pizza, name = get_order(toppings)
    send_to_kitchen(pizza, name)


if __name__ == '__main__':
    main()
