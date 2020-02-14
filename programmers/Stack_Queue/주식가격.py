def solution(prices):
    answer = []
    for i in range(len(prices)): # -1 ???
        cnt = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]: 
                cnt += 1
            else:
                cnt += 1 
                break
        answer.append(cnt)
            
    return answer



# def solution(prices):
#     answer = []
#     for i in range(len(prices)): # -1 ???
#         cnt = 0
#         for j in range(i+1, len(prices)):
#             cnt += 1
#             if prices[i] > prices[j]:
#                 break
#             # if prices[i] <= prices[j]: 
#             #     cnt += 1
#             # else:
#             #     cnt += 1 
#             #     break
#         answer.append(cnt)
            
#     return answer