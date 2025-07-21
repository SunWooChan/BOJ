T = int(input())

for _ in range(T):
	N = int(input())
	a = []

	for _ in range(N):
		a.append(list(map(int,input().split())))

	result = sorted(a, key=lambda x: [x[0], -x[1]])

	count = 1
	tmp = result[0][1]
	for i in range(N-1):
		if tmp > result[i+1][1]:
			count += 1
			tmp = result[i+1][1]
		else:
			continue
	print(count)
