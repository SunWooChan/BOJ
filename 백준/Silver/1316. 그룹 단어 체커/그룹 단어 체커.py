n = int(input())
count = 0

for _ in range(n):
	flag = True
	word = input()
	word_set = set()
	tmp = word[0]
	word_set.add(tmp)

	for i in word[1:]:
		# tmp와 같을 경우
		if i == tmp:
			continue
		# tmp와 다를 경우
		elif i != tmp:
			if i in word_set:
				flag = False
				break
			word_set.add(i)
			tmp = i
	if flag:
		count += 1

print(count)