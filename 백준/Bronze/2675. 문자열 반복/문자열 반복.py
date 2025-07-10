n = int(input())
for i in range(n):
	num, word = input().split()
	words = ""
	for i in word:
		words += i * int(num)
	print(words)
