from sys import exit #NEW

def gold_room() :
	print "This room if full of gold. How much do you take?"

	next_choice = raw_input("> ")
	if "0" in next_choice or "1" in next_choice :
		how_much = int(next_choice)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50 :
		print "Nice, youre not greedy you win!"
		exit(0)
	else :
		dead("You greedy bastard")

def bear_room() :
	print "This room is full of bears. You're fucked!"
	print "These bears have a bunch of honey."
	print "The fat bear is front of another door."
	print "How are you going to move the bear?"

	bear_moved = False

	while True:
		next_choice = raw_input("> ")

		if next_choice == "take honey." :
			dead("The bear eats you up. num num num.")
		elif next_choice == "taunt bear" and not bear_moved :
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next_choice == "taunt bear" and bear_moved :
			dead("Now you pushed your luck. The bear eats your face off.")
		elif next_choice == "open door" and bear_moved :
			gold_room()
		else :
			print "I got no idea what that means."

def cthulhu_room() :
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you until you go insane."
	print "Do you flee for your life or eat your head?"

	next_choice = raw_input("> ")

	if "flee" in next_choice :
		start()
	elif "head" in next_choice :
		dead("Well that was tasty!")
	else :
		cthulhu_room()

def dead(why) :
	print why, "Good job!"
	exit(0)

def start() :
	print "You are in a dark room."
	print "There is a door to your left and another to your right"
	print "Which one do you take?"

	next_choice = raw_input("> ")

	if next_choice == "left" :
		bear_room()
	if next_choice == "right" :
		cthulhu_room()
	else :
		dead("You stumble around until you starve to death.")

start()
