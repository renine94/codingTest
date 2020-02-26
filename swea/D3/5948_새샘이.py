T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    
    res_list = []
    for i in range(7):
        for j in range(1+i, 7):
            for k in range(1+j, 7):
                temp = numbers[i] + numbers[j] + numbers[k]
                res_list.append(temp)
    
    # 정렬
    res_list.sort()

    # 중복제거, 5번째로 큰수
    res = list(set(res_list))[-5]

    print('#{} {}'.format(tc, res))