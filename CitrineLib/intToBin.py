# --------------------------------------------------
#	Function that converts number in base_10 to base_2.
# --------------------------------------------------

def toBinary(num: int):
	'''
		Convert num in base_10 to base_2.
	'''
	s = ""
	while num > 0:
		s = f'{num % 2}{s}'
		num //= 2
	return s

if __name__ == '__main__':
	_bin = toBinary(int(input("num_10 = ")))
	print(f"num_2  = {_bin}")
