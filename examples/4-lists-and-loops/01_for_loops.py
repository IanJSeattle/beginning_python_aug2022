# A for loop is a loop that runs once for each item in an iterable.  An
# iterable is any data type that has a series of things: strings, lists, and
# others we'll discuss in the future.

# A very basic for loop
items = ['one', 'two', 'three', 'four']
for item in items:
    print(item)

# Note the colon at the end of line 7, and the indentation on line 8

# Looping a certain number of times is so common that there's a
# function which exists only to generate a list of numbers.
# This is Python's version of the famous for(i=0; i<10; i++) syntax
# found in other languages
for num in range(10):
    print(num)

# Python has the idea of a slice, which is what it sounds like: a
# partial piece of a list.  A slice is created by giving a normal list
# a start and stop point of what to include:
two_and_three = items[1:3]
print(two_and_three)

# See slice-borders.jpg in this directory

# An empty value before or after the colon character indicates either
# the beginning or end of the list:
one_and_two = items[:2]
print(one_and_two)
three_and_four = items[2:]
print(three_and_four)

# A slice creates a new list without modifying the existing list, so
# it's a quick way to make a copy of a list:
print(id(items))
other_items = items[:]
print(id(other_items))
