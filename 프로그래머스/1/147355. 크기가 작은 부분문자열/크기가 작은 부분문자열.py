def solution(t, p):
    answer = 0
    
    P = len(p)
    a = len(t) // len(p) 
    b = len(t) % len(p)
    r = P * a + b
    for i in range(r-P+1):
        if int(t[i:i+P]) <= int(p):
            print(int(t[i:i+P]))
            answer += 1
    return answer