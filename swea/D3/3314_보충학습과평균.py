T=int(input())
for tc in range(1, T+1):
    scores = list(map(int, input().split()))

    result_list = []
    for score in scores:
        if score <= 40:
            score = 40
            result_list.append(score)
        else:
            result_list.append(score)
    
    result = sum(result_list)//5

    print('#{} {}'.format(tc, result))