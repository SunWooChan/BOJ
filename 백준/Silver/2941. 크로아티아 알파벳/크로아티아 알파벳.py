n = input()

cro = set(['c=','c-','dz=','d-','lj','nj','s=','z='])
arr = []
count = 0

for i in n:
	arr.append(i)
	arr2 = ''.join(arr)
	count += 1

	if arr2[-3:] == 'dz=': # dz= 일 경우
		count -= 2 # 한개 추가
		arr = [] # 초기화
	
	elif arr2[-2:] in cro:
		count -= 1
		arr = []

print(count)
