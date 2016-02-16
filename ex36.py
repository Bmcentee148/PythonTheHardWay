# This is a game based of previous examples for practice. The game will 
# give the user choices based on situations we give them and will
# progress based on those decisions. The user will either end the game
# successfully, or die along the way. The game will terminate in either case.
# 
# Brian McEntee 2.10.16
# version 1

from sys import exit

def space_void() :
    """When the user is floating and asked to go towards earth or the ship."""
    print "You find yourself floating in the vast emptiness of space."
    print "Looking around you, you spot earth in one direction and a space"
    print "shuttle in the other. Which way would you like to go?\n"

    print "(1) Move towards earth."
    print "(2) Move towards the shuttle.\n"

    while True:
        direction_choice = raw_input('> ')
        #print "DEBUG: direction_choice <- %r" % direction_choice
        if direction_choice == '1' :
            print "User chooses to move to earth."
            earth() 
        elif direction_choice == '2' : 
            print "User chooses to move towards the shuttle."
            space_ship()
        else :
            print "Error: Input not recognized."
            print "Type either 1 or 2 and press ENTER."
            direction_choice = ""

def earth() :
    """When the user chooses to boost towards earth"""
    print "Our boosters are in bad shape, how fast should we try and go?\n"

    print "(1) Slow"
    print "(2) Medium"
    print "(3) Fast\n"
    
    
    while True :
        speed_choice = raw_input("> ")
        if speed_choice == '1' :
            print "We will go slow."
            dead("You had terrible timing and got hit by an asteroid. Dead!")
        elif speed_choice == '2' :
            print "We will go medium."
            print "You made it home, but the fuckheads on earth sent you back..."
            space_void()
        elif speed_choice == '3' :
            print "We will go fast."
            dead("You're boosters couldn't handle all that thrust and you died.")
        else : 
            print "Error: Invalid input"
            print "Type either 1, 2, or 3 at the prompt and press ENTER"



def space_ship() :
    """This is when the user chooses to boost to the space ship."""
    print "Boosters aren't looking so great? Should we take it slow?\n"
    print "(1) Slow\n(2) Fast\n"

    speed_choice = raw_input("> ")
    choice_confirmed = False;

    while True:
        if speed_choice == '1' :
            print "You've made it to your ship. Mission complete!"
            exit(0)
        elif speed_choice == '2' :
            dead("You're boosters couldn't handle the thrust, you've died!")
        else :
            print "Error: Invalid input"
            print "Type either 1 or 2 at the prompt and press ENTER"

def dead(reason_why) :
    print reason_why
    exit(0)

space_void()


