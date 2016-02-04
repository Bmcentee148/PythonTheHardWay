#import argv from the sys module so we can use it
from sys import argv

# unpack the args into appropriate variables
script, filename = argv

#open the file and stores returned file object in a var
txt_file = open(filename)

# Tells user what file they are about to view contents of
print "Here's your file %r:" % filename
# prints the contents of the file in entirety
print txt_file.read()

#ask user to print filename again 
print "Print the filename again:"
#prompts user for input and stores it in given var
filename_again = raw_input('> ')

# opens the file again and stores as object in a new var
txt_file_again = open(filename_again)

# prints the contents of the file again that is stored in different var
print txt_file_again.read()

