name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #pounds

eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall" % height
print "He weighs %d pounds" % weight
print "Actually thats not too heavy"
print "He's got %s eyes and %s hair" %(eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

#This line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d" %(
	 height, age, weight, weight + age + height )