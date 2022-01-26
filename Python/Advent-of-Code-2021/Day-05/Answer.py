import numpy as np 

# Part 1: Given a list of coordinates for line segment endpoints,
#			determine how many points are covered by more than 1 line.
#			For now, assume all line segments are vertical or horizontal

# Attempt 1: Gave the correct answer of 6007 but very slowly
with open("input.txt") as file:
	lines = file.read().splitlines()

endpoints = []
for line in lines:
	line = line.split(" -> ")
	line[0] = line[0].split(",")
	line[0][0] = int(line[0][0])
	line[0][1] = int(line[0][1])
	line[1] = line[1].split(",")
	line[1][0] = int(line[1][0])
	line[1][1] = int(line[1][1])
	endpoints.append(line)

one_cover = []
two_cover = []

for pair in endpoints:
	if pair[0][0] == pair[1][0]:
		for i in range(pair[0][1], pair[1][1]):
			point = (pair[0][0], i)
			if point in two_cover:
				pass
			elif point in one_cover:
				two_cover.append(point)
			else:
				one_cover.append(point)
	elif pair[0][1] == pair[1][1]:
		for i in range(min(pair[0][0], pair[1][0]), max(pair[0][0], pair[1][0])+1):
			point = (i, pair[0][1])
			if point in two_cover:
				pass
			elif point in one_cover:
				two_cover.append(point)
			else:
				one_cover.append(point)
	else:

print(len(two_cover))