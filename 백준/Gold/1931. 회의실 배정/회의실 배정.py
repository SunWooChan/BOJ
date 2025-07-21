N = int(input())

a = []
for _ in range(N):
	a.append(list(map(int, input().split())))

result = sorted(a, key=lambda x: (x[1],x[0]))
count = 0
end_time = 0

for i in range(N):
	if result[i][0] >= end_time:
		count+=1
		end_time = result[i][1]
print(count)