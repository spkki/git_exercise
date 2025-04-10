def fibonacci(n):
	fib_sequence = [0, 1]
	while len(fib_sequence) < n:
		fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
	return fib_sequence

if __name__ == "__main__":
	fib_n = int(input("Generate how many Fibonacci numbers? "))
	print(fibonacci(fib_n))
