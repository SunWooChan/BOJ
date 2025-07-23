from itertools import combinations

N, S = map(int,input().split())
lst = list(map(int, input().split()))
ans = 0

for i in range(1,N+1):
	for cur in combinations(lst , i):
		if sum(cur) == S:
			ans += 1

print(ans)