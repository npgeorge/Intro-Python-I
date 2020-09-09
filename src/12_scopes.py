# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

#
# FOUR DIFFERENT SCOPES IN PYTHON
# GLOBAL -- module
# LOCAL -- function
# NONLOCAL (enclosing) -- nested function
# BUILT-IN -- default builtin python methods

# When you use a variable in a function, it's local in scope to the function.
x = 12

# anytime you assign a variable in a function
# it gets asigned a local scope by default 
def change_x():
    global x
    x = 99

change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?

print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)


outer()
