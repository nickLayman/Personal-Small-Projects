import numpy as np

# Part 1: count the number of times the depth increases
#         given the readings in depths.txt

# # Attempt 1: Gave correct answer of 1184
# depths = []
# with open("depths.txt") as file:
# 	for row in file:
# 		depths.append(int(row))
# num_increases = 0
# for i in range(1, len(depths)):
# 	if depths[i] > depths[i-1]:
# 		num_increases += 1
# print(num_increases)

# # Attempt 2: Also correct answer of 1184
# depths = []
# with open("depths.txt") as file:
# 	for row in file:
# 		depths.append(int(row))
# diffs = np.diff(depths)
# print(len(diffs[diffs>0]))

# Attempt 3: Same correct answer but only one pass through the data
increases = 0
with open("depths.txt") as file:
	previous = int(file.readline())
	for row in file:
		current = int(row)
		if current > previous:
			increases += 1
		previous = current
print(increases)



# Part 2: count the number of times the sum of a sliding window
#         of width 3 increases. 
#         depths[i] + depths[i+1] + depths[i+2] > depths[i-1] + depths[i] + depths[i+1]

# # Attempt 2: Gave correct answer of 1158
# depths = []
# with open("depths.txt") as file:
# 	for row in file:
# 		depths.append(int(row))
# window_sums = []
# for i in range(len(depths)-2):
# 	window_sums.append(depths[i] + depths[i+1] + depths[i+2])
# window_diffs = np.diff(window_sums)
# print(len(window_diffs[window_diffs>0]))

# Attempt 2: Based off Part 1 attempt 3
# 		     Gave same correct answer of 1158 with only one pass
increases = 0
with open("depths.txt") as file:
	first = int(file.readline())
	second = int(file.readline())
	third = int(file.readline())
	for row in file:
		new_reading = int(row)
		if new_reading > first:
			increases += 1
		first, second, third = second, third, new_reading
print(increases)