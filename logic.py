solved_array = list(range(1,16))

def isSolvable(arr):
	inversions = 0 
	width = 4     
	row = 0        
	blankrow = 0  

	for i in range(0, len(arr)):
		if i % width == 0:
			row += 1 
		if arr[i] == 0:
			blankrow = row 
			continue

		for j in range(i+1, len(arr)):
			if arr[i] > arr[j] & arr[j] != 0:
				inversions += 1

	if width % 2 == 0:
		if blankrow % 2 == 0:
			return inversions % 2 == 0
		else:
			return inversions % 2 != 0
	else:
		return inversions % 2 == 0

def isSolved(arr):
	return solved_array == arr[:15]
