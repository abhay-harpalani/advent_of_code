import heapq

# with open('test.txt') as f:
# 	lines = f.readlines()
with open('input.txt') as f:
	lines = f.readlines()

# minheaps used in part 1 to get O(log n) remove min
minheap_left = []
minheap_right = []
# dictionaries used in part 2 to get O(1) lookup and edit
dict_left = {}
dict_right = {}

for line in lines:
	# get left and right values from file
	val_left = int(line[:line.find(' ')])
	val_right = int(line[line.rfind(' '):])

	heapq.heappush(minheap_left, val_left)
	heapq.heappush(minheap_right, val_right)

	# count occurences of each value in dict_left and dict_right
	if val_left not in dict_left:
		dict_left[val_left] = 1
	else:
		dict_left[val_left] += 1

	if val_right not in dict_right:
		dict_right[val_right] = 1
	else:
		dict_right[val_right] += 1

# -- part 1 --
diff = 0
# accumulate the differences between the min values of minheap_left and minheap_right
while minheap_left:
	diff += abs(heapq.heappop(minheap_left) - heapq.heappop(minheap_right))
print("part 1:", diff)


# -- part 2 --
similarity_score = 0
# similarity score gets increased by key * val_right, val_left times
for key, val in dict_left.items():
	similarity_score += key * val * dict_right.get(key, 0)
print("part 2:", similarity_score)
