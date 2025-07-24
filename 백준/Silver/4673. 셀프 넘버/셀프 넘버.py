seen=set()

for i in range(1,10000):
	a = []
	for k in str(i):
		a.append(int(k))
	a.append(i)
	seen.add(sum(a))


for i in range(1,10000):
	if i not in seen:
		print(i)