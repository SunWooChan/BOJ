import sys
input = sys.stdin.readline

# 커서를 기준으로 왼쪽 스택과 오른쪽 스택으로 나눔
left = list(input().strip())  # 커서 왼쪽
right = []  # 커서 오른쪽

N = int(input())
for _ in range(N):
    command = input().strip()
    
    if command == 'L':
        if left:  # 왼쪽에 문자가 있으면
            right.append(left.pop())  # 왼쪽 끝을 오른쪽으로
    
    elif command == 'D':
        if right:  # 오른쪽에 문자가 있으면
            left.append(right.pop())  # 오른쪽 끝을 왼쪽으로
    
    elif command == 'B':
        if left:  # 왼쪽에 문자가 있으면
            left.pop()  # 왼쪽 끝 삭제
    
    else:  # P $
        left.append(command[2])  # 왼쪽에 추가

# 결과 출력
print(''.join(left + right[::-1]))