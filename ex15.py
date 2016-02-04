from sys import argv

script, filename = argv

txt_file = open(filename)

print "Here's your file %r:" % filename
print txt_file.read()

print "Print the filename again:"
filename_again = raw_input('> ')

txt_file_again = open(filename_again)

print txt_file_again.read()

