# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE
def f1(x, y):
    z = x + y
    print(z)

print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE
def f2(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

# using another method
def f2_a(*args):
    print("f2 args", args)
    return sum(args)

print(f2_a(1))                    # Should print 1
print(f2_a(1, 3))                 # Should print 4
print(f2_a(1, 4, -12))            # Should print -7
print(f2_a(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
print(f2(*a))    # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE
def f3(*args):
    result = 0
    length = len(args)
    if length == 1:
        for x in args:
            result = x + 1
    elif length == 2:
        for x in args:
            result += x
    return result

# another way
def f3_2(a, b=1):
    return a + b

print('--F3 Here--')
print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9

print('--F3_2 Here--')
print(f3_2(1, 2))  # Should print 3
print(f3_2(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# YOUR CODE HERE
def f4(*args,**kwargs):
    print('--What are the kwargs??---')
    print("kwargs: ", kwargs) 
    # get key value pairs
    print('---Key, Value Pairs!---')
    for keys in kwargs:
        print('key: ', keys, ', value: ', kwargs[keys])

def f4_2(**kwargs):
    for k, v in kwargs.items():
        print(f'key: {k}, value: {v}')  

# Should print
# key: a, value: 12
# key: b, value: 30
print('---f4---')
f4(a=12, b=30)
print('---f4_2---')
f4_2(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
f4(**d)

# double star for keyword arguments
# single star for arbitrary positional arguments
