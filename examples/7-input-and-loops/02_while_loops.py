# A while loop is very similar to a for loop, but also very different.
# Instead of using data from an iterator, it checks a condition you specify to
# figure out how long to loop.  Here's a basic while loop:

response = ''
count = 1
while response != 'y':
    print(f'Current count is {count}.')
    response = input('Had enough yet? ')
q_word = 'question' if count == 1 else 'questions'
print(f'You had enough after {count} {q_word}')

# See that q_word definition?  That's the closest Python gets to the trinary
# operator (x = condition ? true_option : false_option) from C-like languages.

# While loops test a condition.  Above, that condition was, "Has the user
# answered 'y' to the question?"  A condition can be anything that evaluates
# to True or False in a boolean context (that is, anything can be used as a
# condition, since any thing in Python will be either True or False).

# Static flag.  Note that this will run forever.
beers = 0
while True:
    bottle_word = 'bottle' if beers == 1 else 'bottles'
    print('{beers} {bottle_word} of beer on the wall')
    beers += 1

# Static flag with a break.  This won't run forever (usually important).
beers = 0
while True:
    bottle_word = 'bottle' if beers == 1 else 'bottles'
    print('{beers} {bottle_word} of beer on the wall')
    beers += 1
    if beers > 99:
        break

# The break keyword causes the current loop to exit immediately.

# Internal condition.  Note that the while loop runs "as long as (condition)
# is true."
beers = 0
while beers <= 99:
    bottle_word = 'bottle' if beers == 1 else 'bottles'
    print('{beers} {bottle_word} of beer on the wall')
    beers += 1

# Sometimes you just need the user to say something.
response = ''
while not response:
    print('Please say something')
    response = input('What do you think? ')

# The "break" and "continue" keywords give you some control over a loop.
# break will stop the loop and resume execution at the next instruction after
# the loop, while continue will cause the current iteration of the loop to
# end, and restart back at the top, continuing the looping behavior.
beers = 99
while beers > 0:
    bottle_word = 'bottle' if beers == 1 else 'bottles'
    print(f'{beers} {bottle_word} of beer on the wall')
    response = input('Take one down and pass it around? ')
    if response == 'y':
        beers -= 1
        continue
    else:
        response = input('Had enough yet? ')
        if response == 'y':
            break

# Make sure any while loop you write will actually end, if you don't intend it
# to run forever:
#
# * The while condition will eventually be set to a falsey value
# * The loop contiains a break instruction that will definitely run
