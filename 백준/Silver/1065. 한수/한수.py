N = int(input())

count = 0
for n in range(1, N+1):
	a = []
	if n <= 99:
		count += 1
		continue

	for i in str(n):
		a.append(int(i))

	ok = True
	diff = a[1]-a[0]

	for i in range(1, len(a)-1):
		if a[i+1] - a[i] != diff:
			ok = False
			break
		if ok:
			count+=1

print(count)
