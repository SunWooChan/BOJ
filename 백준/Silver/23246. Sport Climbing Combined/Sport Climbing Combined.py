n = int(input())
lst = []
for _ in range(n):
	a = list(map(int, input().split(' ')))
	lst.append(a)

# 곱한 것 오름차순, 더한것 오름차순, 등번호 오름차순
result = sorted(lst, key = lambda x: [x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]])

print(result[0][0], result[1][0], result[2][0])