# This one is like your scripts with argv
def print_two(*args) :
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# This way to print out two arguments is preferred
def print_two_better(arg1, arg2) :
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# This one takes a single argument
def print_one(arg1) :
	print "arg1: %r" % arg1

# This one doesn't take an argument at all
def print_none() :
	print "I got nothin."

print_two("Brian", "McEntee")
print_two_better("Zed", "Shaw")
print_one("Single")
print_none()



