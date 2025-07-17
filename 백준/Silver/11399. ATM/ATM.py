n = int(input())
lst = list(map(int,input().split()))
result = sorted(lst)
a=0
b = []
# 1 2 3 3 4
for i in result:
	a += i
	b.append(a)

print(sum(b))
