name = "Zed A. Shaw"
age = 35 # not a lie
print "Let's talk about %s." % name

height = 74 # inches
height_centimeters = height * 2.54
print "He's %d inches, or %d centimeters tall." % (height, round(height_centimeters))

weight = 180 # pounds
weight_kilograms = weight * 0.453592
print "He's %d pounds, or %d kilograms heavy." % (weight, round(weight_kilograms))
print "Actually, thats not too heavy."

eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + weight + height) 

