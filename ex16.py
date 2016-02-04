# A simple text editor

#
#	target_file	-> file we will truncate and write to as a File Object
#	script_name	-> Name of the script as a String
#	file_name 	-> the name of the file we will deal with as a String
#	line_*		-> a line of text received from user as a String
#

from sys import argv

script_name, file_name = argv # unpack command line args

print "We're going to erase %r." % file_name
print "If you don't want that, hit CTRL-C (^C)."
print "If you do, hit RETURN."

raw_input("?")

print "Opening the file..."
target_file = open(file_name, 'w')

print "Truncating the file. Goodbye!"
target_file.truncate()

print "Now I am going to ask you for three lines."

line_1 = raw_input("Line 1: ")
line_2 = raw_input("Line 2: ")
line_3 = raw_input("Line 3: ")

print "I am going to write these to the target file."

target_file.write(line_1)
target_file.write('\n')
target_file.write(line_2)
target_file.write('\n')
target_file.write(line_3)
target_file.write('\n')

print "And finally we'll close it"
target_file.close()

