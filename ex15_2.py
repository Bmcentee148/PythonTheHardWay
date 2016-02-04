from sys import argv

script, filename = argv

txt_file = open(filename)

print "Here's your file %r:" % filename
print txt_file.read()

print "Print the filename again:"
filename_again = raw_input('> ')

txt_file_again = open(filename_again)
print "This time I will only show you the first two lines of the file."
line1 = txt_file_again.readline() 
line2 = txt_file_again.readline() 
print line1
print line2

txt_file.close()
txt_file_again.close()

