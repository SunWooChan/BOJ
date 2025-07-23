from itertools import permutations

n = input()
ans = 0

# set()을 사용하지 않고 바로 처리
seen = set()  # 이미 확인한 순열 저장

for cur in permutations(n, len(n)):
    # 튜플을 문자열로 변환하여 중복 체크
    cur_str = ''.join(cur)
    if cur_str in seen:
        continue
    seen.add(cur_str)
    
    ok = True
    for i in range(len(n)-1):
        if cur[i] == cur[i+1]:
            ok = False
            break
    if ok:
        ans += 1

print(ans)