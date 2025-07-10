n = int(input())
count = 0

for _ in range(n):
	word = input()
	tmp = []
	flag = True

	for w in word:
		
		if len(tmp)==0:
			tmp.append(w)
		
		elif w == tmp[-1]:
			continue

		elif w in tmp:
			flag = False
			break

		else:
			tmp.append(w)

	if flag == True:
		count+=1

print(count)