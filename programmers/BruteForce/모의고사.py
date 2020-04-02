def solution(answers):
    answer = []

    supo = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    temp = []
    for s in supo:
        idx = 0
        cnt = 0
        for a in answers:
            if a == s[idx]:
                cnt += 1
            idx += 1
            if idx == len(s):
                idx = 0
        temp.append(cnt)

    # temp => 수포1,2,3 들이 맞은 갯수
    maxV = max(temp)
    for idx, t in enumerate(temp):
        if t == maxV:
            answer.append(idx+1)

    return answer
