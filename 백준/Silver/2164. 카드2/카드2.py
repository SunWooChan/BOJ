from collections import deque

n = int(input())
stack = deque()

for i in range(1, n+1):
	stack.append(i)

while len(stack) != 1:
	stack.popleft()
	stack.append(stack[0])
	stack.popleft()

print(stack[0])