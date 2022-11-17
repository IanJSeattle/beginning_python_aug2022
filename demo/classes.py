class Pizza:
    sizes = ['small', 'medium', 'large', 'gigantic']
    size = ''
    toppings = None
    num_slices = 0

    def __init__(self, size=''):
        self.size = size

pep_pizza = Pizza()

for item in pep_pizza:
    print(item)
