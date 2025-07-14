while True:
    try:
        n = input()
        stack = []
        if n == ".":
            break
        is_valid = True
        for i in n:
            if i == "(":
                stack.append(i)
            elif i == ")":
                if stack and stack[-1] == "(":  # 수정
                    stack.pop()
                else:
                    is_valid = False
            elif i == "[":  # elif로 수정
                stack.append(i)
            elif i == "]":
                if stack and stack[-1] == "[":  # 수정
                    stack.pop()
                else:
                    is_valid = False
        if len(stack)==0 and is_valid:  # 수정
            print("yes")
        else:
            print("no")
    except:
        break