from collections import deque

t = int(input())

for _ in range(t):
	n = int(input())
	card = deque(list(map(str, input().split())))
	answer = deque()
	answer.append(card.popleft())
	a = len(card)
	for _ in range(len(card)):
		if card[0] <= answer[0]:
			answer.appendleft(card.popleft())
		else:
			answer.append(card.popleft())

	print(''.join(answer))