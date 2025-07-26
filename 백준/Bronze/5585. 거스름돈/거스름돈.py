n = int(input())
n = 1000 - n

count = 0
result = 0
change = [500, 100, 50, 10, 5, 1]

for i in change:
	count = n // i
	n -= i * count
	result += count

print(result)
