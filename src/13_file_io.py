"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# using the with method automatically closes files
with open('foo.txt') as f:
    read_data = f.read()
    print('--Reading File....--')
    print(read_data)
    print('--File Read Completed...--')

# checking that it automatically closed the file
print('Is the file closed?: ', f.closed)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar = open("bar.txt", "w")
bar.write("Blee \nBloo \nBlah")
bar.close()

with open('bar.txt') as f:
    read_lines = f.read()
    print('--Reading File....--')
    print(read_lines)
    print('--File Read Completed....--')