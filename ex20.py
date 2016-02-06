from sys import argv

script_name, input_file_name = argv

def print_all(file_to_print) :
	print file_to_print.read()

def rewind(file_to_rewind) :
	beginning_file_byte = 0
	file_to_rewind.seek(beginning_file_byte)

def print_a_line(line_count, file_to_print) :
	print line_count, file_to_print.readline(),

# Lets open the file and store it in an appropriate variable
current_file = open(input_file_name)

# Now, lets print the entire contents of the file
print "Printing the entire contents of the file:\n"
print_all(current_file)

# If we want to read from it again we need to set the pointer back to the
# beginning of the file
print "Now we are rewinding the pointer of the file to the beginning."
rewind(current_file)

print "Now we will print out some lines from the file singularly."
# Lets print out a single line from the file
current_line = 1
print_a_line(current_line, current_file)

# And how about the second line now
current_line+=1
print_a_line(current_line, current_file)

# And finally lets print the third line
current_line+=1
print_a_line(current_line, current_file)

# Close the file we opened!
current_file.close()