def fibo():
	s = 0
	a = 1  # Represents the current Fibonacci number being processed
	b = 2  # Represents the next Fibonacci number in the sequence
	while a <= 4000000:
		if a % 2 == 0:
			s += a
		a, b = b, a + b
	return str(s)


if __name__ == "__main__":
        print(fibo())
