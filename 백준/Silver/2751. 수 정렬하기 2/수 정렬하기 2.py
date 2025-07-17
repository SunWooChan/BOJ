n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

result = sorted(a)
for i in result:
    print(i)