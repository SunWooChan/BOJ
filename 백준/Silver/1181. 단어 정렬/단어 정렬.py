n = int(input())
arr = []

for _ in range(n):
	arr.append(input())
arr = set(arr)
arr = sorted(arr, key=lambda x: x.lower())
arr = sorted(arr, key=lambda x: len(x))

for i in arr:
	print(i)
