# Accessing data in a dict one at a time is good, but how about putting this
# into a loop?  Here's how to access all the pieces of a dict.

hours_of_sleep = {
    'Sunday': 8,
    'Monday': 7,
    'Tuesday': 5,
    'Wednesday': 9,
    'Thursday': 6,
    'Friday': 9,
    'Saturday': 6,
}

my_keys = hours_of_sleep.keys()

my_values = hours_of_sleep.values()

# These produce a 'dict_keys' or 'dict_value' type, which is similar to a
# list, but isn't quite a list.  However, it acts enough like a list that you
# can use it in a for loop.

for day in hours_of_sleep.keys():
    hours = hours_of_sleep[day]
    print(f'I got {hours} hours of sleep on {day}')

# Note that the above loop and this following loop act exactly the same: the
# .keys() method is the default action when you loop over a dict.

for day in hours_of_sleep:
    hours = hours_of_sleep[day]
    print(f'I got {hours} hours of sleep on {day}')

# .values(), meanwhile, gives you just the values

total = 0
for hours in hours_of_sleep.values():
    total += hours
print(f'I got {total} hours of sleep total')

# One of the most useful of these, however, is .items(), which gives you both
# keys and values, like so:

for day, hours in hours_of_sleep.items():
    print(f'I got {hours} hours of sleep on {day}')

# Like lists, dicts can contain lists or dicts, making a "multi-dimensional"
# data structure.  This one is a dict containing dicts.

sales = {
    'Jan 1': {'pizzas': 252.38, 'sodas': 192.20, 'other': 299.21},
    'Jan 2': {'pizzas': 298.68, 'sodas': 185.41, 'other': 249.33},
    'Jan 3': {'pizzas': 185.22, 'sodas': 122.48, 'other': 175.44},
    'Jan 4': {'pizzas': 412.91, 'sodas': 299.91, 'other': 281.90},
    'Jan 5': {'pizzas': 102.71, 'sodas': 188.71, 'other': 104.80},
    'Jan 6': {'pizzas': 281.18, 'sodas': 278.88, 'other': 301.28},
}

print(sales['Jan 1'])

# Just like lists, a dict can be created using a comprehension.  Use curly
# braces {} instead of square brackets [] (which make a list).

squares = {i: i**2 for i in range(10)}
print(squares)
