# --------------------------------------------------
#	The Sieve of Eratosthenes.
# --------------------------------------------------

def prime_sieve(number: int):
	'''
		Return a list of prime numbers from 0 to number.
	'''
	sieve = [x for x in range(number)]
	sieve[1] = 0

	for i in range(2, number):
		if sieve[i] != 0:
			j = i * 2
			while j < number:
				sieve[j] = 0
				j += i

	return [el for el in sieve if el != 0]

if __name__ == '__main__':
	result = sieve(int(input("Find all prime numbers from 0 to ")))
	print(f"Prime numbers are:\n{result}")
