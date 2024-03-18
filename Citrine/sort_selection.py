# --------------------------------------------------
#	Selection sort algorithm.
# --------------------------------------------------

def findSmallest(array):
	smallest = array[0]
	smallest_index = 0
	for i in range(1, len(array)):
		if array[i] < smallest:
			smallest = array[i]
			smallest_index = i
	return smallest_index

def selectionSortUp(_array):
	sorted = []
	for _ in range(len(_array)):
		smallest = findSmallest(_array)
		sorted.append(_array.pop(smallest))
	return sorted

def findBiggest(array):
	biggest = array[0]
	biggest_index = 0
	for i in range(1, len(array)):
		if array[i] > biggest:
			biggest = array[i]
			biggest_index = i
	return biggest_index

def selectionSortDown(_array):
	sorted = []
	for _ in range(len(_array)):
		biggest = findBiggest(_array)
		sorted.append(_array.pop(biggest))
	return sorted

if __name__ == '__main__':
	array1 = [4, 6, 2, 7, 4, 25, 6, 0]
	array2 = [4, 6, 2, 7, 4, 25, 6, 0]

	print("\n  UP : " + str(selectionSortUp(array1)) + "\nDOWN : " + str(selectionSortDown(array2)))
