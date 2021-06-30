import hangman as h

"""
Hangman game loop goes here.
TODO: add an actual hangman
TODO: add UI for funzies
TODO: input validation for guesses; split validation function
TODO: cleanup the game code. Store logic in modules file
"""

if __name__ == "__main__":

	# counter is hardcoded for now
	counter = 5

	hidden_word = h.prompt_for_word()
	exposed_word = h.hide_word(hidden_word)

	asked_letters = []

	print("And now for the main event.")
	while True:

		print(f"{h.print_dashes(exposed_word)}\n")

		while True:
			guess = h.letter_input()
			if len(guess) == 1:
				if h.asked_letter_validation(guess, asked_letters) == False:
					asked_letters.append(guess)
					break
				else:
					print(f"Letter {guess} was already asked. No penalty.")
			elif len(guess) > 1:
				break # breaks with guess being a word

		if len(guess) == 1:
			# procedure for a letter
			positions = h.letter_lookup(hidden_word, guess)

			exposed_word = h.expose_word_partially(exposed_word, guess, positions)

			counter = h.failure_counter(positions, counter)
		else: 
			# procedure for a word
			if guess == hidden_word:
				exposed_word = []
				for char in guess:
					exposed_word.append(char)

			else:
				print(f"Word was incorrect. Down goes the counter.")
				counter -= 1


		is_game_over = h.game_over(exposed_word, counter)
		if is_game_over:
			if counter <= 0:
				print(f"Aw. Too bad that you've been hanged.")
			else:
				print(f"Hooray! Word was guessed.")
			print(f"Game over! Word: {hidden_word}")
			print(f"Your word: {h.print_dashes(exposed_word)}")
			print(f"Asked letters: {asked_letters}")
			break

else:
	print("Oh hey. Hangman was imported.")
