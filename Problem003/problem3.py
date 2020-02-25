
x=600851475143
y=0
i=2
while i <= x:
    if x % i == 0:
        x /= i
        y = i
    else:
        i += 1
print("The answer is", y)
