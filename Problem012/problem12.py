def compute():
	triangle,n = 0,1
	while 1:
		triangle += n
		n+=1
		if num_divisors(triangle) == 500:
			return str(triangle)
def num_divisors(n):
	count=0
	for i in range(1,n):
		if n%i==0:
			count+=1
	return count		
if __name__ == "__main__":
	print(compute())