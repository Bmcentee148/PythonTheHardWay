def cheese_and_crackers(cheese_count, boxes_of_crackers) :
	print "You have %s cheeses" % cheese_count
	print "You have %s cracker boxes" % boxes_of_crackers
	print "Man thats enough for a party"
	print "Get a blanket\n"

print "We can just put our values directly into the function."
cheese_and_crackers(20, 30)

print "OR, we can pass the function variables that we have created instead"
cheese_amount = 20
crackers_amount = 30

cheese_and_crackers(cheese_amount, crackers_amount)

print "We can use math as arguments as well."
cheese_and_crackers(10 + 20, 20 + 30)

print "And we can combine the two, math and variables"
cheese_and_crackers(10 + cheese_amount, 20 + crackers_amount)




