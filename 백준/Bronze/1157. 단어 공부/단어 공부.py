words = input().upper()
dic = {}
for word in words:
	if word in dic:
		dic[word] += 1
	else:
		dic[word] = 1

max_count = max(dic.values())

answer = []
for w, c in dic.items():
	if c == max_count:
		answer.append(w)

if len(answer) == 1:
	print(answer[0])
else:
	print('?')

