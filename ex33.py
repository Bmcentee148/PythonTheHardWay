# Here we will be working with while loops.

# Function Definitions
def add_nums(lst, max_num, increment) :
	i = 0
	while i < max_num :
		lst.append(i)
		i += increment

def add_nums_forloop(lst, max_num,increment) :
	for i in range(0,max_num,increment) :
		lst.append(i) 

# Beginning of the script
numbers = []

print "First let's add some numbers with the while loop method."
add_nums(numbers,20,2)

print "The list currently contains: ", numbers

print "Now we'll use the for loop method, adding the same numbers to the curr list."
add_nums_forloop(numbers,20,2)

print "Numbers at finish: ", numbers

#while i < 6 :
#	print "At the top i is: %r" % i
#	numbers.append(i)
#
#	i += 1
#	print "Numbers now: ", numbers
#
#	print "At the bottom i is: %r" % i
# end while



# We could also print the numbers this way
#for num in numbers :
#	print num