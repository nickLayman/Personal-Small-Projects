import numpy as np

# Part 1: given directions like "forward 5" or "down 3"
#         determine the horizontal position and depth
#         of the submarine after all instructions are followed
#         then return the product of your horizontal position and depth

# Attempt 1: Gave correct answer of 2117664
horizontal = 0
depth = 0
with open("input.txt") as file:
	for row in file:
		directions = row.split(" ")
		if directions[0] == "forward":
			horizontal += int(directions[1])
		elif directions[0] == "down":
			depth += int(directions[1])
		elif directions[0] == "up":
			depth -= int(directions[1])
print(horizontal*depth)



# Part 2: The commands must be reinterpreted
#		 down X increases your aim by X units.
#		 up X decreases your aim by X units.
#		 forward X does two things:
#		 	It increases your horizontal position by X units.
#		 	It increases your depth by your aim multiplied by X.

# Attempt 1: Gave correct answer of 2073416724
horizontal = 0
depth = 0
aim = 0
with open("input.txt") as file:
	for row in file:
		directions = row.split(" ")
		if directions[0] == "forward":
			horizontal += int(directions[1])
			depth += aim*int(directions[1])
		elif directions[0] == "down":
			aim += int(directions[1])
		elif directions[0] == "up":
			aim -= int(directions[1])
print(horizontal*depth)