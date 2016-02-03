# first line of phrase
x = "There are %d types of people." % 10
# variable to store word binary in string format
binary = "binary"
# variable to store word for do not in string format
do_not = "don't"
#second line of the phrase
y = "Those who know %s and those who %s." % (binary, do_not)

#print the first line of the phrase
print x
#print the second line of the phrase
print y

# show what we printed for first line in raw string format 
print "I said: %r" % x
# show what we printed for the second line and place in quotes
print "I also said: '%s'." % y

# boolean value to store if joke is funny or not
hilarious = False
# a joke evaluation in string format, must be given an argument for printing
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the joke evaluation string given our value of hilarious
print joke_evaluation % hilarious

w = "this is the left side of a string..."
e = "this is the right side of a string..."

#concatentates w and e and creates on string, which is printed
print w + e

