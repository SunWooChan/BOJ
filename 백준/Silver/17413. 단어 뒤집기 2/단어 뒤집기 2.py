s = str(input())
result = []
word = []
tag = False

for i in s:
	if i == '<': # 태그 시작
		if word:    # 태그 시작 전 단어 처리
			result.extend(word[::-1])
			word = []
		tag = True
		result.append(i) # 태그 < 추가
	
	elif i == '>': # 태그 끝
		tag = False
		result.append(i) # 태그 > 추가
	
	elif tag == True:  # 태그 안 문자는 그냥 추가
		result.append(i)

	elif i == ' ': # 띄어쓰기 만났을 때
		result.extend(word[::-1]) # word 거꾸로해서 stack에 추가
		result.append(' ')
		word = [] # word 초기화
	
	else: 
		word.append(i) # 일반 단어는 word에 추가

if word:
	result.extend(word[::-1])

print(''.join(result))