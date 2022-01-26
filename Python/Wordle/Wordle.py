answers = []
guesses = []
with open("wordle-answers-alphabetical.txt", 'r') as file:
	for line in file.readlines():
		answers.append(line.strip())
		guesses.append(line.strip())
with open("wordle-allowed-guesses.txt", 'r') as file:
	for line in file.readlines():
		guesses.append(line.strip())


def respond(true_word, guess_word):
	response = []
	for index in range(len(guess_word)):
		guess_letter = guess_word[index]
		true_letter = true_word[index]
		if guess_letter == true_letter:
			response.append(2)
		elif guess_letter in true_word:
			response.append(1)
		else:
			response.append(0)
	return response


def valid_word(test_word, guess_word, response):
	for index in range(len(response)):
		guess_letter = guess_word[index]
		test_letter = test_word[index]
		letter_response = response[index]
		if (letter_response == 0) and (guess_letter in test_word):
			return False
		elif (letter_response == 1) and (guess_letter not in test_word):
			return False
		elif (letter_response == 2) and (guess_letter != test_letter):
			return False
	return True


def reduce(guess_word, response):
	global answers
	new_answers = []
	for word in answers:
		if valid_word(word, guess_word, response):
			new_answers.append(word)
	return new_answers


def count_valid_words(guess_word, response):
	global answers 
	count = 0
	for word in answers:
		if valid_word(word, guess_word, response):
			count += 1
	return count


def worst_true_word(guess_word):
	global answers
	worst_word = max(answers, key = lambda a: count_valid_words(guess_word, respond(a, guess_word)))
	return worst_word, count_valid_words(guess_word, respond(worst_word, guess_word))


def best_guess():
	global answers 
	global guesses 
	best_word = min(guesses, key = lambda g: worst_true_word(g)[1])
	return best_word, worst_true_word(best_word)

print(best_guess())