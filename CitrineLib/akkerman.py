# --------------------------------------------------
#	Akkerman's recursive function.
# --------------------------------------------------

from sys import setrecursionlimit

setrecursionlimit(5000)

def akk(m: int, n: int):
	if m == 0:
		return n + 1
	elif m > 0 and n == 0:
		return akk(m - 1, n)
	return akk(m - 1, akk(m, n - 1))

if __name__ == '__main__':
	for i in range(10):
		print("------------------------------")
		for j in range(10):
			print(f"akk({i}, {j}) = {akk(i, j)}")
	print("------------------------------")
