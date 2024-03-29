# --------------------------------------------------
#	Quick sort algorithm.
# --------------------------------------------------

def qsort(array):
	if len(array) < 2:
		return array
	middle = len(array) // 2
	middle_el = array[middle]
	smaller = []
	bigger = []
	for i in range(len(array)):
		if array[i] < middle_el:
			smaller.append(array[i])
		elif i != middle:
			bigger.append(array[i])
	return qsort(smaller) + [middle_el] + qsort(bigger)

if __name__ == '__main__':
	array = [3, 6, 1, 8, 3, 7, 0, 1, 9]
	print(qsort(array))