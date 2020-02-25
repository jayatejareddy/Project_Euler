import math
def compute():
	sol = 1
	for x in range(1, 21):
		sol *= x // math.gcd(x, sol)
	return sol


if __name__ == "__main__":
	print(compute())
