# Interacting with users on the console (as opposed to via a graphical
# interface) is quite simple, and we'll stick with the console for this class.
# So far, we've told the user things, but never asked them for input.  Here's
# how to request information from a user.

prompt = 'What is your name? '  # note the trailing space
response = input(prompt)
print(f'Your name is {response}')

# The input() function always returns a string, even if the user enters
# numbers.  Remember to convert with int() or float() if you need to do math
# on a user's answer.

response = input('What is your favorite number? ')
print(f'Your favorite number is {response}, which is a {type(response)}')
