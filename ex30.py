num_people = 30
num_cars = 40
num_buses = 15

if num_cars > num_people :
	print "We should take the cars."
elif num_cars < num_people :
	print "We should not take the cars."
else : 
	print "We can't decide."

if num_buses > num_cars :
	print "That's too many buses."
elif num_buses < num_cars : 
	print "Maybe we could take the buses actually."
else : 
	print "We still can't decide."

if num_people > num_buses :
	print "Alright, let's just take the damn buses."
else :
	print "Okay nevermind, let's just stay home then."