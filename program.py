import math
answer = math.factorial(100)
answer = str(answer)
total = 0
for char in answer:
	total += int(char)

print total
