import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().strip().split())
count = 0

deq = deque()
for i in range(1,n+1):
	deq.append(i)

a = list(map(int, input().strip().split()))

for i in a:
	# print("i:", i)
	# print(deq)
	# print("i index:", deq.index(i))

	if deq.index(i) > len(deq)//2:
		while i!=deq[0]:
			# deq.append(deq.popleft())
			deq.rotate(1)
			count+=1
	else:
		while i!=deq[0]:
			# deq.appendleft(deq.pop())
			deq.rotate(-1)
			count+=1
	
	if i == deq[0]:
		deq.popleft()
	# print("count: ",count)
	# print()

print(count)
