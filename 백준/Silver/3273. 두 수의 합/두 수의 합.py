n = int(input())
lst = list(map(int, input().split()))
x = int(input())

count = 0
seen = set()

for num in lst:
    if x - num in seen:
        count += 1
    seen.add(num)

print(count)