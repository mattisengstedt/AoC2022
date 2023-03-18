import csv

A = rock = 1
B = paper = 2
C = scissor = 3
X = loss = 0
Z = draw = 3
Y = win = 6

score = 0

with open('input.csv', 'r') as f:
	reader = csv.reader(f, delimiter = ' ')
	matches = list(reader)
	currentrow = 0
	for x in matches:
		if x[0] == str('A'):
			if x[1] == str('X'):
				score += + loss + scissor

			elif x[1] == str('Y'):
				score += + draw + rock

			elif x[1] == str('Z'):
				score += + win + paper

		elif x[0] == str('B'):
			if x[1] == str('X'):
				score += + loss + rock

			elif x[1] == str('Y'):
				score += + draw + paper

			elif x[1] == str('Z'):
				score += + win + scissor

		elif x[0] == str('C'):
			if x[1] == str('X'):
				score += + loss + paper

			elif x[1] == str('Y'):
				score += + draw + scissor

			elif x[1] == str('Z'):
				score += + win + rock

		currentrow += 1


	print(score)