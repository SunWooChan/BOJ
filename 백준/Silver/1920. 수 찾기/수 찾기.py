n = int(input())
N = set(map(int, input().split()))

m = int(input())
M = list(map(int, input().split()))

# N (1 2 3 4 5) 가 M (1 3 5 7 9) 안에 있어야 함

for i in M:
	if i in N:
		print(1)
	else:
		print(0)
