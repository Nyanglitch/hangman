import hangman as h

"""
Hangman game loop goes here.
TODO: add a feature to ask either a letter or guess the whole word
TODO: add an actual hangman
TODO: add UI for funzies
"""

# counter is hardcoded for now
counter = 5

hidden_word = h.prompt_for_word()
exposed_word = h.hide_word(hidden_word)

print("And now for the main event.")
while True:

	print(f"{h.print_dashes(exposed_word)}\n")

	# guesses need an array of already asked letters
	# i.e. no duplicates please
	guess = h.letter_input()

	positions = h.letter_lookup(hidden_word, guess)

	exposed_word = h.expose_word_partially(exposed_word, guess, positions)

	counter = h.failure_counter(positions, counter)

	# gameover module:
	# doesn't need to say anything when checking
	# needs to distinguish between bad end and good end
	is_game_over = h.game_over(exposed_word, counter)
	if is_game_over:
		print(f"Game over! Word: {hidden_word}")
		print(f"Your array: {h.print_dashes(exposed_word)}")
		break