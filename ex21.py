def add(val_1, val_2) :
	print "Adding %r and %r" % (val_1, val_2)
	return val_1 + val_2

def subtract(val_1, val_2) :
	print "Subtracting %r from %r" % (val_2, val_1)
	return val_1 - val_2

def multiply(val_1, val_2) :
	print "Multiplying %r and %r together." % (val_1, val_2)
	return val_1 * val_2

def divide(val_1, val_2) :
	print "Dividing %r by %r" % (val_1, val_2)
	return float(val_1 / val_2)

print "Let's do some math with just functions."

vals_sum = add(30, 5)
print vals_sum
vals_difference = subtract(78, 4)
print vals_difference
vals_product = multiply(90, 2)
print vals_product
vals_quotient = divide(100, 2)
print vals_quotient

# A puzzle for extra credit
print "Here is a puzzle"

what = add(vals_sum, subtract(vals_difference, multiply(vals_product, 
	divide(vals_quotient,2))))

print "That becomes:", what, " Can you do it by hand?"

print "How about 10 + (85 / (2 + 6.5)) ?"
print add(10, divide(85, add(2,6.5)))