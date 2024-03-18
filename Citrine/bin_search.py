# --------------------------------------------------
#	Function that converts number in base_10 to base_2.
# --------------------------------------------------

from random import randint

def isSorted(array: list, direction: str):
	'''
		Return 1 if array is sorted according to direction, 0 if not, -1 if direction is invalid. \\
		Direction is "up" or "down".
	'''
	if direction != "up" and direction != "down":
		print(f"Invalid directiion \"{direction}\"")
		return -1
	for i in range(len(array) - 1):
		if (array[i] <= array[i + 1] and direction == "down") or (array[i] >= array[i + 1] and direction == "up"):
			print("Array is not propperly sorted.")
			return 0
	return 1

def binarySearch(array: list, value: int):
	'''
		Binary search in sorted array.
	'''
	if isSorted(array, "up") == 0:
		array = list(set(array))

	left = 0
	right = len(array) - 1
	pos = len(array) // 2

	print(f"\nArray:\t\t{array}\nSearching for:\t{value}")
	while left <= right:
		if array[pos] == value:
			print(f"Item \"{value}\" found at index [{pos}].")
			return pos
		elif array[pos] > value:
			right = pos - 1
		else:
			left = pos + 1
		pos = (left + right) // 2
	if left > right:
		print(f"Item \"{value}\" not found.")
		return -1

if __name__ == '__main__':
	_list = [randint(0, 10) for x in range(randint(1, 10))]
	value = randint(0, 5)
	binarySearch(_list, value)
