# Combining argv (command line args) with raw_input() to form a bigger program

from sys import argv

script, input_file_name = argv

output_file_name = raw_input("Name the file you wish to export to: ")

print "The user would like to copy the contents of %s into a file named %s" % (
	input_file_name, output_file_name)
