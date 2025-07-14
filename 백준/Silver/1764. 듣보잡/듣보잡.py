N, M = map(int, input().split())

# 듣
a = []
b = []
for i in range(N):
	a.append(input())
# 보
for j in range(M):
	b.append(input())

# 듣보 확인
result = list(set(a) & set(b))

# 사전 순 출력
result.sort(key=str.lower)
print(len(result))
for i in result:
	print(i)