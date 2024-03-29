# --------------------------------------------------
#	Function that converts number in base_10 to base_2.
# --------------------------------------------------

def is_sorted(_array: list, _ascending: bool = True) -> bool:
	'''
		Return "True" if array is sorted according to direction, "False" if not. \\
		Direction is "True" for Ascending (default) and "False" for Descending.
	'''
	for i in range(len(_array) - 1):
		print(_array[i], _array[i + 1])
		print(_array[i] <= _array[i + 1], not _ascending)
		print(_array[i] >= _array[i + 1], _ascending)
		print((_array[i] <= _array[i + 1] and not _ascending) or (_array[i] >= _array[i + 1] and _ascending))
		print()
		# if (_array[i] <= _array[i + 1] and not _ascending) or (_array[i] >= _array[i + 1] and _ascending):
		if not (_array[i] <= _array[i + 1] and _ascending) or not (_array[i] >= _array[i + 1] and not _ascending):
			return False
	return True


def binary_search(_array: list, _value: int) -> int:
	'''
		Binary search in sorted array.
	'''
	print(is_sorted(_array), is_sorted(_array, False), not is_sorted(_array) and not is_sorted(_array, False))
	if not is_sorted(_array) and not is_sorted(_array, False):
		return -1
	
	

	left = 0
	right = len(_array) - 1
	pos = len(_array) // 2

	while left <= right:
		if _array[pos] == _value:
			return pos
		elif _array[pos] > _value:
			right = pos - 1
		else:
			left = pos + 1
		pos = (left + right) // 2
	if left > right:
		return -1

if __name__ == '__main__':
	from random import randint

	# _list = sorted([randint(0, 10) for x in range(randint(1, 10))])
	# _value = randint(0, 5)
	_list = [0,0,1]
	_value = 1

	print(is_sorted(_list))

	# x = binary_search(_list, _value)
	# print(_list, _value, x)
