# This will copy the contents of one file to another
# Study drill to clean up the code in ex17.py

from sys import argv
from os.path import exists

script_name, to_file_name, from_file_name = argv # unpack command line args

# Start small asshole, don't jump the gun
#in_file_contents = open(from_file_name).read()
open(to_file_name, 'w').write(open(from_file_name).read())

print "Alright, all done."



