def pens_and_books(num_pens, num_books) :
	print "So you have %s pens, and %s books" % (num_pens, num_books)

pens_and_books(10,20)

num_start_pens = 2
num_start_books = 5

# passing just variables
pens_and_books(num_start_pens, num_start_books)

# passing just some math
pens_and_books(5 + 15, 0 + 2)

# passing math and variables
pens_and_books(num_start_pens + 10, num_start_books + 50)

# passing random strings instead of expected input
pens_and_books("unexpected_1", "unexpected_2")

# passing some floating point values
pens_and_books( 5.0 / 2.0, 10.0 / 4.0)
