import sys
input = sys.stdin.readline
from collections import deque


n = int(input().strip())
origin = deque()
floor = deque()
for i in range(1,n+1):
	floor.appendleft(i)
# floor = [5, 4, 3, 2, 1]
skill = list(map(int, input().strip().split()))

for i in reversed(skill):
	if i == 1: # 바닥 제일 위 -> 원본 제일 위
		origin.append(floor.pop())

	elif i == 2: # 바닥 -> 원본 위에서 두번째 카드
		if len(origin) > 0:
			tmp = origin.pop()
			origin.append(floor.pop()) # 바닥 카드를 위로 올리고
			origin.append(tmp) # 위에서 한장 뺀걸 다시 위로		
		else:
			origin.append(floor.pop())

	elif i == 3: # 바닥 -> 원본 제일 밑의 카드
		origin.appendleft(floor.pop())

print(*reversed(origin))
