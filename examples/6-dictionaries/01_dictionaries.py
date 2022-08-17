# A dictionary (commonly called a dict) is like a list, except instead of a
# numerical index, the dictionary takes an arbitrary, immutable value as a
# key.  This is like a mini-database.  Create a new dictionary with curly
# braces, {}, and separate keys and values with a colon instead of a comma.
my_dict = {'name': 'Laura', 'position': 'Python teacher'}

# Dict keys can be any immutable value:
key1 = 5
key2 = 'hello'
key3 = ('Laura', 'Johnston')

# Mutable values can't be used:
badkey1 = ['one', 'two', 'three']
badkey2 = {'name': 'Laura', 'position': 'Python teacher'}

# Access values in a dict with similar syntax to what you use for a list
print(my_dict['name'])

# Adding a key-value pair to a dict is easy
my_dict['location'] = 'Seattle'

# Modifying the value associated with a key is equally easy
my_dict['name'] = 'Laura Johnston'

# Deleting a value is the same as for a list
del my_dict['location']
