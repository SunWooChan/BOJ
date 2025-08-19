def solution(my_string):
    string = ['0','1','2','3','4','5','6','7','8','9']
    num = []
    for i in my_string:
        if i in string:
            num.append(int(i))
    answer = sorted(num)
    return answer