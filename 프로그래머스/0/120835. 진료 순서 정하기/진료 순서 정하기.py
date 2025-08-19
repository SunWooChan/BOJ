def solution(emergency):
    answer = []
    a = sorted(emergency, reverse=True)
    arr = []
    for i in range(len(a)):
        arr.append((i+1, a[i]))
    
    for j in emergency:
        for i in arr: # [(1, 76), (2, 24), (3, 3)]
            if j == i[1]: # 76=76
                answer.append(i[0])
    return answer