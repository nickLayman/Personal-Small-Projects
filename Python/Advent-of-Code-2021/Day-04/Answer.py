import numpy as np 

# Part 1: playing bingo with a squid
#			Given a set of 100 5x5 bingo boards (all positive integers)
#			and a known sequence of called numbers, 
#			determine which board will win first (diagonals do not win)
#			Then determine the score of that win
#			Score = (sum of uncalled numbers on board) * (most recent call)

# Attempt 1: Gave correct answer of 50008
#				Feels slow and inefficient
#				I'm tracking called numbers and rechecking boards
#				instead of keeping markers on the boards
with open("input.txt", 'r') as file:
	lines = file.read().splitlines()

draws = np.array(lines[0].split(','), dtype=int)

boards = np.empty((100, 5, 5), dtype=int)
for i in range(100):
	for j in range(5):
		boards[i, j] = np.array(lines[6*i+2+j].strip().split())

def board_win(board, called_nums):
	# row win
	row_win = np.any(np.all(np.isin(board, called_nums), 1))
	column_win = np.any(np.all(np.isin(board, called_nums), 0))
	return row_win or column_win

def score(board, called_nums):
	bool_board = np.isin(board, called_nums)
	return np.sum(board*(1-bool_board))*called_nums[-1]

def answer(draws):
	for i in range(len(draws)):
		called_nums = draws[:i+1]
		for board in boards:
			if board_win(board, called_nums):
				return score(board, called_nums)
	return False

print(answer(draws))


# Part 2: Figure out which board will win last and 
#			determine it's score once it wins

# Attempt 1: Gave correct answer of 17408

def first_nonwinning_board(boards, called_nums):
	for board in boards:
		if not board_win(board, called_nums):
			return board
	return False

def answer(draws):
	for i in range(len(draws)):
		called_nums = draws[:len(draws)-i]
		for board in boards:
			if not board_win(board, called_nums):
				return score(board, draws[:len(draws)-i+1])
	return False

print(answer(draws))