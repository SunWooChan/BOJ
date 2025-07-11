n = int(input())

for _ in range(n):
	a = list(input())
	stack = []
	flag = True

	for C in a:
		if C == '(':
			stack.append(C)
		elif C == ')': 
			if not stack or stack[-1] != '(':
				print("NO") # 스택이 비거나 ( 가 나왔을 때
				flag = False
				break
			stack.pop()

	if flag and len(stack) == 0:
		print("YES")
	elif flag:
		print("NO") # ((( 만 나왔을 때
