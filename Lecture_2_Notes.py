# Lecture Notes 2

# FUNCTIONS

#
# ex.) 1
#
print('----- ex. 1 -----')
def mult2(x,y):
    print(f"{x} is being multiplied by {y}")
    return x*y

print(mult2(2,7))

a = 12
print(mult2(a, 6))

b = 11

#
# ex.) 2
#
print('----- ex. 2 -----')
def foo(x):
    print(x) # this will print 8
    x = 12
    print(x) # this will print 12

# immutable type
a = 8

# integers/value assigns are NOT CHANGEABLE 
# we can't change this assignment
foo(a)

print(a)

#
# ex.) 3
#
print('----- ex. 3 -----')
# we're not changing x here, 
# we're pointing it to a new place in memory
def foo(x):
    x[2] = 99

# mutable type
a = [1,2,3,4]

# lists/arrays are mutable, we can CHANGE whats in there
foo(a) # this is really mutating this one array

print(a[2])

#
# string examples
#
print('---string example---')

# this will throw an error
# strings are IMMUTABLE, and can not be changed
s='hello'
#s[2] = 'X'

#
# ex.) 4
#
print('----- ex. 4 -----')
# x effectively creates another instance of the string
def foo(x):
    print(x)
    x = x.upper()
    print(x)

# immutable type
a = "hello"

foo(a)

print(a)

#
# UPER!
#

# Return the "centered" average of an array of positive or negative ints, which
# we'll say is the mean average of the values, except ignoring the largest and 
# smallest values in the array. The array can be out of order. The array will 
# have at least 3 numbers.

# centered_average([1,2,3,4,100]) -> 3
# centered_average([1,1,5,5,10,8,7]) -> 5
# centered_average([1,2,3,4]) -> 5/2 = 2.5

def centered_average(a):
    print('Input: ', a)
    a.sort()
    print('Sorted: ', a)

    # remember slices are
    middle = a[1:-1] # slicing index 1 to index 1 from the end

    total = 0
    for v in middle:
        total += v
    
    return total // len(middle)

print('---1st function---')
print(centered_average([1, 1, 5, 5, 10, 8, 7]))

def centered_average2(a):
    a.remove(max(a))
    a.remove(min(a))

    total = 0
    for v in a:
        total += v
    
    return total // len(a)

print('---2nd function---')
print(centered_average2([1, 1, 5, 5, 10, 8, 7]))
