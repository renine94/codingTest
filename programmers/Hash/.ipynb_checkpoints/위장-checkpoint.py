# 문제
# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    
    # box라는 dict 생성후, 각 옷의 종류가 몇개인지 카운트
    # ex) box = {'headgear': 2, 'eyewear': 1}
    box = {}
    for name, cate in clothes:
        if cate not in box:
            box[cate] = 1
        else:
            box[cate] += 1
    
    # +1 을 해주는이유는 각 종류의 옷을 안입을 수도 있기 때문
    temp = []
    for val in box.values():
        temp.append(val+1)
    
    # 각 종류별로 독립적이므로 서로 곱해주고
    for v in temp:
        answer *= v
    
    # 모두 안입는 경우는 없으므로 -1
    return answer - 1


#####################################
# 다른풀이
#####################################
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1 # 3번째 인자 초기값 x에 들어가게됨
    return answer