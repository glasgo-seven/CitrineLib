# --------------------------------------------------
#	Some useful functions for matrixes.
# --------------------------------------------------

from random import randint

matrix = [[randint(-10, 10) for x in range(5)] for y in range(5)]

def print_matrix(matrix: list):
	'''
		Prints matrix. Wow!
	'''
	for line in matrix:
		for item in line:
			print(f'{item:>5}', end = '')
		print()

def get_sumOfElements(matrix: list):
	'''
		Print matrix with additional: \\
		column for sum of elements in a row; \\
		row for a sum of elements in a column.
	'''
	sum_column = [0] * len(matrix[0])

	for line in matrix:
		sum_line = 0
		for i, item in enumerate(line):
			sum_line += item
			sum_column[i] += item

			print(f'{item:>5}', end = '')
		
		print(f" | {sum_line}")

	print('-' * len(matrix) * 6)

	for s in sum_column:
		print(f'{s:>5}', end = '')

def swap_diagonals(matrix):
	'''
		Spaws main and sub diagonals in a matrix.
	'''
	for i in range(len(matrix[0])):
		for j in range(len(matrix[0])):
			if i == j:
				matrix[i][j], matrix[i][len(matrix) - 1 - j] = matrix[i][len(matrix) - 1 - j], matrix[i][j]

if __name__ == '__main__':
	print_matrix(matrix)
	print()
	get_sumOfElements(matrix)
	print()
	swap_diagonals(matrix)
	print()
	print_matrix(matrix)