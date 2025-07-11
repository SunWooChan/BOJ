
word = list(input())

croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
stack = []
count = 0

for i in word:
	stack.append(i)
	count += 1
	if len(stack)==1:
		continue
	elif len(stack)>= 3 and stack[-3]+stack[-2]+stack[-1] in croatian :
			count -=2
			stack.pop()	
			stack.pop()	
			stack.pop()
			stack.append('X')
	elif len(stack)>=2 and stack[-2]+stack[-1] in croatian:
			count -=1
			stack.pop()	
			stack.pop()	
			stack.append('X')

print(count)