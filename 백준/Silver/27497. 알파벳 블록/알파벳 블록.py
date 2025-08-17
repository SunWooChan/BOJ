from collections import deque
import sys
input = sys.stdin.readline


n = int(input().strip())
answer = deque()
tmp = []
for _ in range(n):
	a = list(map(str,input().strip().split()))

	if a[0] == '1': # 뒤
		answer.append(a[1])
		tmp.append((a[1],1))
	elif a[0] == '2': # 앞
		answer.appendleft(a[1])
		tmp.append((a[1],0))
	else:
		if len(answer)>0:
			rm = tmp.pop()
			if rm[1] == 0:
				answer.popleft()
			else:
				answer.pop()
if len(answer)==0:
	print(0)
else:
	print(''.join(answer))
