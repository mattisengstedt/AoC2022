import csv

with open('input.csv', 'r') as f:
	reader = csv.reader(f)
	blocks = []
	current_block = []
	for row in reader:
		if row:
			current_block.append(int(row[0]))
		else:
			blocks.append(current_block)
			current_block = []
	blocks.append(current_block)

blocks_sums = [sum(block) for block in blocks]

blocks_sums.sort()

max_index = blocks_sums.index(max(blocks_sums))

print(blocks_sums[max_index]+blocks_sums[max_index-1]+blocks_sums[max_index-2])
