n = int(input())
lst = []
for _ in range(n):
	a,b = map(int, input().split())
	lst.append((a,b))

result = sorted(lst)

for i in result:
	print(i[0], i[1])