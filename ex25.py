def break_words(stuff) :
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words) :
	"""Sort the words."""
	return sorted(words)

def print_first_word(words) :
	"""Prints the first word after popping it off."""
	first_word = words.pop(0)
	print first_word

def print_last_word(words) :
	"""Prints the last word after popping it off."""
	last_word = words.pop(-1)
	print last_word

def sort_sentence(sentence) :
	"""Take in a full sentence and return the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence) :
	"""Prints the first and last words in the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence) :
	"""Sorts the sentence and prints the first and last words."""
	sorted_words = sort_sentence(sentence)
	print_first_word(sorted_words)
	print_last_word(sorted_words)
