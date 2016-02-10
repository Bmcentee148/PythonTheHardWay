print "You enter a dark room with two doors. Do you go through door #1",
print "or door #2?"

# Keep the input as a string rather than convert to int so we can allow the user
# to enter alternative choices
door_chosen = raw_input("> ") 

if door_chosen == '1' :
	print "Theres a giant bear sitting here eating cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear"
	
	plan_taken = raw_input("> ")

	if plan_taken == '1' :
		print "The bear eats your face off. Good job!"
	elif plan_taken == '2' :
		print "The bear eats your legs off. Good job!"
	else :
		print "Well, doing %s is probably better. Bear runs away." % plan_taken

elif door_chosen == '2' :
	print "You stare into the endless abyss as Cthula's retina."
	print "1. Blueberries"
	print "2. Yellow Jacket Clothespins"
	print "3. Understanding revolvers yelling melodies."

	users_insanity = raw_input("> ")

	if users_insanity == '1' or users_insanity == '2' :
		print "Your body survives powered by a mind of jello. Congrats!"
	else :
		print "The insanity rots your eyes in a pool of muck!"

else :
	print "Your stumble around, fall on a knife, and die like a bitch."


