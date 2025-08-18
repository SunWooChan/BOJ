def solution(strings, n):
    answer = sorted(strings, key=lambda x:(x[n],x))
    # answer = []
    return answer