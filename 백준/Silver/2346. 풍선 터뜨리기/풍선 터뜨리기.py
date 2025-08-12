from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))

baloon = []
for i in range(len(arr)):
	baloon.append((arr[i],i+1))

dq = deque(baloon)
answer = []
for i in range(n):
	a = dq.popleft()
	answer.append(a[1])

	if dq:
		if a[0] > 0:
			dq.rotate(-a[0]+1)
		else:
			dq.rotate(-a[0])

print(*answer)
