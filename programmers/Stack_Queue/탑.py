def solution(heights):
    answer = []
    for i in range(len(heights)):
        #for j in range(시작, 끝점, -1)
        for j in range(i, -1, -1):
            if heights[i] < heights[j]: # 현재 탑보다 비교탑이 높을때
                answer.append(j+1)
                break
        else:
            answer.append(0)

    return answer


#  # 다른풀이
# def solution(heights):
#     answer = []
    
#     for i in range(len(heights)):
#         stack = []
#         for j in range(i):
#             if heights[i] < heights[j]:
#                 stack.append(j+1) # 인덱스만 들어있는 스택
#         if len(stack) != 0:
#             answer.append(stack.pop())
#         else:
#             answer.append(0)
#     return answer