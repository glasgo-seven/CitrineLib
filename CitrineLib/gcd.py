# --------------------------------------------------
#	Three different aproaches for searching greatest common divisor.
# --------------------------------------------------

def gcd_1(a: int, b: int):
	while a != b:
		if a > b:
			a -= b
		else:
			b -= a
	return a

def gcd_2(a: int, b: int):
	if a == 0:
		return b
	return gcd_2(b % a, a)

def gcd_3(a: int, b: int):
	while a != 0:
		b, a = a, b % a
	return b

if __name__ == '__main__':
	print("\n-INPUTS---------------------------")
	a = int(input("  Number 1 = "))
	b = int(input("  Number 2 = "))
	print("\n-RESULTS--------------------------")
	print(f"  Loop & Subtraction:\tgcd = {gcd_1(a, b)}")
	print(f"  Recursion & Modulo:\tgcd = {gcd_2(a, b)}")
	print(f"  Loop & Modulo:\tgcd = {gcd_3(a, b)}")
	print("\n")
