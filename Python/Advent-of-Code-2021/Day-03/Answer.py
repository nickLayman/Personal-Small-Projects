import numpy as np 

# Part 1: The input is a list of length 12 binary numbers
#          Determine the most common first bit, second bit, etc
#          The most common bits when interpreted as binary give gamma
#          The least common bits when interpreted as binary give epsilon
#          Return gamma*epsilon for the power consumption

# Attempt 1: Gave correct answer of 4191876 but feels a bit clumsy
# Gamma and epsilon will always be the complement of each other (bit inversion)
# So we only need to calculate the Gamma bits
# To determine most common bit, add up all the bits
# and compare the sum to the number of readings. 
# If the sum is more than half, then 1 is most common
num_readings = 0
bit_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
with open("input.txt") as file:
	for row in file:
		num_readings += 1
		for i in range(12):
			bit_sum[i] += int(row[i])
gamma_bin = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
epsilon_bin = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(12):
	if bit_sum[i] > num_readings/2:
		gamma_bin[i] = 1
	else:
		epsilon_bin[i] = 1
gamma, epsilon = 0, 0
for i in range(12):
	gamma += 2**(11-i)*gamma_bin[i]
	epsilon += 2**(11-i)*epsilon_bin[i]
print(gamma_bin, gamma*epsilon)
# could be improved by, instead of taking the sum,
# when the input is 1, add 1 but when it's 0 substract 1
# then gamma is determined by whether the bit sum is positive or negative
# not much cleaner but a bit better



# Part 2: Filter the input bits
#          if the first bit matches the most common first bit, keep it and discard the rest
#          if only one number remains, stop. That is the oxygen generator rating
#          else, move to the next bit and keep filtering
#          For the CO2 scrubber rating, do the same but the least common bits
#          Return the product of the oxygen generator rating and the CO2 scrubber rating
#          If 0 and 1 are equally common, call 1 more common

# # Attempt 1:
# # Determine most common bits the same way as above
# # but with my slight improvement written after Attempt 1
# bit_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# with open("input.txt") as file:
# 	for row in file:
# 		for i in range(12):
# 			if int(row[i]) == 1:
# 				bit_sum[i] += 1
# 			else:
# 				bit_sum[i] -= 1
# most_common = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(12):
# 	if bit_sum[i] >= 0:
# 		most_common[i] = 1
# 	else:
# 		most_common[i] = 0

# # Now we start filtering
# # Instead of maybe doing 24 passes, we can keep track of which
# # input number matches or mismatches the most start bits
# # if the current number is more then we keep it, otherwise we discard it
# def count_matches(row):
# 	# How far into most_common does row match?
# 	i = 0
# 	while i<12 and (int(row[i]) == most_common[i]):
# 		i += 1
# 	return i

# def count_mismatches(row):
# 	# How far into most_common does row mismatch?
# 	i = 0
# 	while i<12 and (int(row[i]) != most_common[i]):
# 		i += 1
# 	return i

# with open("input.txt") as file:
# 	this_row = file.readline()
# 	most_matches = str(this_row)
# 	num_matches = count_matches(most_matches)
# 	most_mismatches = str(this_row)
# 	num_mismatches = count_mismatches(most_mismatches)
# 	for row in file:
# 		if count_matches(row) > num_matches:
# 			most_matches = str(row)
# 			num_matches = count_matches(row)
# 		if count_mismatches(row) > num_mismatches:
# 			most_mismatches = str(row)
# 			num_mismatches = count_mismatches(row)

# # Now, if there exists a unique solution to this, we have it
# # Now to convert to decimal
# print(most_common, most_matches, most_mismatches)
# # most_matches = int(''.join(most_matches), 2)
# # most_mismatches = int(''.join(most_mismatches), 2)
# most_matches_num = 0
# most_mismatches_num = 0
# for i in range(12):
# 	most_matches_num += 2**(11-i)*int(most_matches[i])
# 	most_mismatches_num += 2**(11-i)*int(most_mismatches[i])
# print(most_matches_num, most_mismatches_num, most_matches_num*most_mismatches_num)



# Attempt 2:
# Attempt 1 was wrong because I am meant to recalculate
# the most/least common bit value after each filter
# instead of using the most/least common value of the whole set
def MCV(data, i):
	count = 0
	for num in data:
		if num[i] == "1":
			count += 1
		else:
			count -= 1
	if count>=0:
		return "1"
	return "0"

most_common = []
least_common = []
with open("input.txt") as file:
	for row in file:
		most_common.append(row)
		least_common.append(row)

i=0
while len(most_common) > 1:
	most_common = list(filter(lambda num: num[i] == MCV(most_common, i), most_common))
	i += 1
i=0
while len(least_common) > 1:
	least_common = list(filter(lambda num: num[i] != MCV(least_common, i), least_common))
	i += 1

print(int(most_common[0], 2)*int(least_common[0], 2))