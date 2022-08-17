# To use code from another module, you need to import that module first, like
# so:

import 03_modules

# This imports 03_modules into this program's namespace.  More on namespace
# below.  To then use the code from the imported module, you reference both
# the imported module name, and the function you want to use from the module:

03_modules.say_hello()

03_modules.say_something('Using this imported function!')

# Let's say the module you need to import has an awkward name (ahem), and you
# don't want to have to type it out a lot of times.  You can import individual
# functions from the module, then call them directly, like so:

from 03_modules import say_something

say_something('Now using a named function from the other module!')

# But if you need everything from the module, and don't feel like naming every
# last thing in your import statement, you can alias the module's name using
# the "as" keyword.

import 03_modules as mod

mod.say_something('Now using an aliased module name!')

mod.make_pizza('pepperoni', 'pickled peppers', deliver_to='Peter Piper')

# It's important to note that when you import a module, Python actually runs
# its code.  Any code in the module will be executed.  Go back and look at
# 03_modules.py: nothing runs, it just defines some functions and ends.  Try
# importing this file into the interpreter.  What happens?
