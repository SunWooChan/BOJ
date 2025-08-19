def solution(numbers):
    answer = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i]*numbers[j] >= answer:
                answer = numbers[i]*numbers[j]
            else:
                continue
    return answer