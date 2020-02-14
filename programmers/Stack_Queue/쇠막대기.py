def solution(arrangement):
    answer = 0
    stack = 0
    for index, i in enumerate(arrangement):
        if i == ')':
            stack -= 1
            if arrangement[index-1] == ')':
                answer += 1
            else:
                answer += stack
        else:
            stack += 1
    return answer

solution('()(((()())(())()))(())')


# 문제 분석 중요
# 글로부터 도출
