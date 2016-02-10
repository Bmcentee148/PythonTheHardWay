the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of loop goes through a list

for num in the_count :
	print "This is count: %d" % num

for fruit in fruits : 
	print "A fruit of type: %s" % fruit

# We can go through lists that contain mixed types too.
# Notice though that we need to use the %r formatter because we do not know
# what types of items are stored.
for some_item in change :
	print "I got %r change back." % some_item

# We can also build lists. Start with an empty one like this:
my_list = []

# We will use the range(...) function to do 0 to 5 counts and fill the list
#for num in range(0,6) :
#	print "Adding %d to the list." % num
#	my_list.append(num)

my_list = range(0,6) # this way is much cleaner than above with same results

# Now we can print them out too
for item in my_list :
	print "Element was: %d" % item