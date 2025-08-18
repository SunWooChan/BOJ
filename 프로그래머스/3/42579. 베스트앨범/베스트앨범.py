def solution(genres, plays): # 장르, 재생 횟수
    tup = ()
    dic = {}
    tup = [(i, genres[i], plays[i]) for i in range(len(genres))]
    
    for k, v in zip(genres, plays):
        if k in dic:
            dic[k] += v
        else:
            dic[k] = v
    
    dic = sorted(dic.items(), key=lambda x:-x[1])
    dicc = []
    for i in dic:
        dicc.append(i[0])
    
    # dic의 첫번째 key 뽑기
    # dic의 첫번째 Key를 가진 tuple에서 가장 많은 수를 가진 인덱스 뽑기
    # 하나하면 한개 뽑고 두개 이하로만 뽑기
    # for i in tup:
    answer = []
    for genre in dicc:
        songs = []
        for i, g, p in tup:
            if g == genre:
                songs.append((i, p))
        
        songs.sort(key=lambda x: (-x[1],x[0]))
        
        for i in range(min(2,len(songs))):
            answer.append(songs[i][0])
    
    return answer # 고유 번호 순서대로