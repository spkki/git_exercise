def is_prime(num):
	if num < 2:
		return False
	for i in range(2, int(num**0.5) + 1):
		if num % i == 0:
			return False
		return True

def get_primes(n):
	primes = []
	for i in range(m, n+1):
		if is_prime(i):
			primes.append(i)
	return primes

if __name__ == "__main__":
	m = int(input("Start prime search from:  "))
	n = int(input("Find primes up to: "))
<<<<<<< HEAD
	print(get_primes(m, n))
=======
	print(get_primes(m, n))
	print(f"Number of primes found: {len(get_primes(m, n))}")
>>>>>>> origin/master
