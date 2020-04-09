T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 수열의 길이, 개수

    lst = list(map(int, input().split())) # 2 3 4 5
    for _ in range(M-1):
        n_lst = list(map(int, input().split())) # 4 8 7 6 
        for i in range(len(lst)):
            if n_lst[0] < lst[i]:
                lst[i:i] = n_lst
                break
        else:
            lst.extend(n_lst)

    result = lst[::-1][:10]
    print('#{}'.format(tc), *result)


'''
로직은 맞으나 시간초과, 리스트에서 나누고 합치는과정이 너무많음
'''
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # 수열의 길이, 개수

#     temp = list(map(int, input().split())) # 2 3 4 5

#     for _ in range(M-1):
#         arr = list(map(int, input().split())) # 4 8 7 6 
#         for idx, val in enumerate(temp):
#             if val > arr[0]:
#                 a = temp[:idx]
#                 b = temp[idx:]
#                 a.extend(arr)
#                 a.extend(b)
#                 temp = a
#                 break
#         else:
#             temp.extend(arr)
    
#     result = temp[::-1][:10]

#     print('#{}'.format(tc), *result)