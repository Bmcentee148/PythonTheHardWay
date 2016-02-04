# This will read the contents of the file we wrote to in ex16.py

from sys import argv

script_name, file_name = argv # unpack command line args

file_for_reading = open(file_name)

print file_for_reading.read()