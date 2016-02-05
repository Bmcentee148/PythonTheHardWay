# This will copy the contents of one file to another

from sys import argv
from os.path import exists

script_name, to_file_name, from_file_name = argv # unpack command line args

print "Copying from %s to %s" % (to_file_name, from_file_name)

# This could be done in one line instead, but how?
# in_file_contents = open(from_file_name).read() ? 
in_file = open(from_file_name)
in_file_contents = in_file.read()

print "The input file is %d bytes long." % len(in_file_contents)

print "Does the output file exist? %r" % exists(to_file_name)
print "Ready, hit RETURN to continue or CTRL-C to abort."
raw_input()

out_file = open(to_file_name, 'w')
out_file.write(in_file_contents)

print "Alright, all done."

out_file.close()
in_file.close()

