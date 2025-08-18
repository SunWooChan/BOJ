n = input().split('-')
ans = sum(map(int, n[0].split('+')))
for i in n[1:]:
	if '+' in i:
		ans -= sum(map(int, i.split('+')))
	else:
		ans -= int(i)
print(ans)