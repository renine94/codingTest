# 프로그래머스 해시
# 문제 - https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    
    temp = {}
    temp2 = {}
    
    # 장르와 플레이수를 zip으로 묶기
    genres_plays = list(zip(genres, plays))
    # print(genres_plays)
    
    # temp 에 장르별 플레이 횟수 구하기
    for genre, play in genres_plays:
        if genre in temp:
            temp[genre] += play
        else:
            temp[genre] = play
    
    # temp2 에 장르마다 고유번호(idx) 와 플레이수 담기
    for idx, values in enumerate(genres_plays):
        if values[0] in temp2:
            temp2[values[0]].append((idx, values[1]))
        else:
            temp2[values[0]] = [(idx, values[1])]
    
    # 장르별 플레이 횟수를, 플레이횟수로 정렬하기
    temp = dict(sorted(temp.items(), key=lambda x:x[1], reverse=True))
    # print(temp)
    # print(temp2)
    
    # 정렬된 temp 에서 장르(keys) 꺼내오면서,
    # temp2 장르에 저장된 고유번호와 플레이 수를 플레이 수로 정렬하고,
    # 정렬된 lst 에서 고유번호 앞에꺼 2개만 정답에 넣어주기
    for key in temp.keys():
        lst = temp2[key]
        lst = sorted(lst, key=lambda x:x[1], reverse=True)
        for idx, val in lst[:2]:
            answer.append(idx)
    
    
    return answer