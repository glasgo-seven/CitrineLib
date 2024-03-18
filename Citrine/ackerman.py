# --------------------------------------------------
#	Ackerman's recursive function.
# --------------------------------------------------

from sys import setrecursionlimit

setrecursionlimit(5000)

def ack(m: int, n: int):
	if m == 0:
		return n + 1
	elif m > 0 and n == 0:
		return ack(m - 1, n)
	return ack(m - 1, ack(m, n - 1))

if __name__ == '__main__':
	for i in range(10):
		print("------------------------------")
		for j in range(10):
			print(f"ack({i}, {j}) = {ack(i, j)}")
	print("------------------------------")
