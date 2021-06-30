"""
Module full of function definitions
that make up the hangman game.
"""

import getpass

def prompt_for_word():
	"""
	Prompts user for word and returns it.
	"""
	valid = False
	while not valid:
		word = getpass.getpass(prompt="Word to hide: ")
		valid = word_validation(word)
	return word

def word_validation(word):
	"""
	Validates the word for having
	only allowed characters.
	"""
	allowed_chars = []
	for i in range(97, 123): # generates alphabet
		allowed_chars.append(chr(i))
		
	valid = False
	for char in word:
		if char not in allowed_chars:
			valid = False
			return valid
		else:
			valid = True
	return valid

def hide_word(word):
	"""
	Takes in a word and 'hides' it;
	Creates and returns an array of dashes.
	"""
	exposed = []
	for letter in word:
		exposed.append("_")
	return exposed

def print_dashes(exposed_array):
	"""
	Takes in an array of dashes and returns them
	in a nice string. Purely decorative.
	"""
	decorated_string = ""
	for dash in exposed_array:
		decorated_string = decorated_string + dash + " "
	return decorated_string

def letter_input():
	"""
	Prompts user for a letter. Returns it.
	"""
	letter = input("Letter guess: ")
	return letter

def asked_letter_validation(letter, larray):
	'''
	Takes in a letter and a letter array.
	Returns true if the letter is present
	in the array, false if not.
	'''
	if letter in larray:
		return True
	else:
		return False

def letter_lookup(word, letter):
	"""
	Takes in a letter and a word and seeks it in the word.
	Returns letter positions list if true,
	returns empty list if false. 
	"""
	positions = [i for i, j in enumerate(word) if j == letter]
	return positions

def expose_word_partially(hidden_word, letter, positions):
	"""
	Takes in an array of dashes, a letter and positions.
	Substitutes dashes on given positions with letters.
	Returns a partially uncovered array of dashes
	and letters.
	"""
	for i, dash in enumerate(hidden_word):
		if i in positions:
			hidden_word[i] = letter

	return hidden_word

def failure_counter(positions, counter):
	"""
	Takes in positions returned from letter_lookup,
	passes if not false, reduces counter if false.
	Returns counter (possible from max to 0)
	"""
	if counter == 0:
		# print("Game over.")
		return 0

	if not positions:
		counter -= 1
		print("Down goes the counter.")
		return counter
	else:
		return counter

def hangman_printout():
	"""
	With every call yields a part of hanged man.
	"""
	pass

def game_over(hidden_word, counter):
	"""
	LOGIC MODULE
	Takes in counter and dash array.
	If counter is 0 - game ends.
	If dash array is fully exposed - game ends.
	"""
	gameover = False

	if counter == 0:
		gameover = True
		# print("Counter reached zero, you've been hanged.")
		return gameover

	for dash in hidden_word:
		if dash == "_":
			# print("Word isn't fully uncovered.")
			gameover = False
			return gameover
		else:
			gameover = True

	return gameover
