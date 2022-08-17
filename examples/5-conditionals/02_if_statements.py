# If statements use boolean values to control the flow of a program.
if True:
    print('True: the if statement ran this code!')

if False:
    print('False: the if statement ran this code!')

# The if statement converts whatever you give it into a boolean value, using
# those truthiness rules from earlier.
if 7.2:
    print('7.2: the if statement ran this code!')

if 0:
    print('0: the if statement ran this code!')

if 'hello, world!':
    print('"hello, world!": the if statement ran this code!')

if '':
    print('"": the if statement ran this code!')

# == returns a boolean, but its friends also return boolean values
print(5 > 2)
print(5 >= 6)
print(5 != 8)
print('hello' != 'world')

# So, you can use these in if statements to perform conditional logic
for i in range(10):
    if i > 5:
        print(f'{i}: we got a whopper!')

# You can use the "and" and "or" keywords to combine conditions to be tested
for i in range(10):
    if i > 5 and i < 8:
        print(f'{i} is between 5 and 8')
    if i % 2 == 0 and i != 0:
        print(f'{i} is an even number')

