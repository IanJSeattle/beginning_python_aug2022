# Python provides two easy ways to sort lists: sort() and sorted()
#
# Why two? One (sort()) is a method of a list object, while the other
# (sorted()) is an independent function, that can sort anything, even things
# that aren't lists.  They also treat their subject lists differently.

my_list = [7, 2, 5, 9, 3]

# First, using sorted()
sorted_list = sorted(my_list)
print(my_list)
print(sorted_list)

# Now, using sort(). Can you see the important way they're different?
my_list.sort()
print(my_list)

# An example of using sorted() on something other than a list
sorted_string = sorted('hello')
print(sorted_string)
