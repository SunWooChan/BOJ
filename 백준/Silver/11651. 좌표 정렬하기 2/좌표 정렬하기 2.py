n = int(input())
a = []
for _ in range(n):
	b = list(map(int, input().split()))
	a.append(b)

result = sorted(a, key=lambda x: [x[1], x[0]])
for i in result:
	print(i[0], i[1])