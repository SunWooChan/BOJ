N = int(input())
lst = []
for _ in range(N):
	lst.append(int(input()))

# 평균
print(round(sum(lst)/N))

# 중앙값
result = sorted(lst)
print(result[len(result)//2])


# 최빈값
count = {}
for i in result:
	count[i] = count.get(i, 0) + 1
value = sorted(count.items(), key=lambda x: -x[1])
if len(value)>=2 and value[0][1] == value[1][1]:
	print(value[1][0])
else: 
	print(value[0][0])

# 범위
print(result[-1] - result[0])