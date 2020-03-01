T = int(input())
for tc in range(1, T+1):
    data = input()
    # print(data)

    people = 0
    cnt = 0
    for idx, val in enumerate(data):
        people += int(val)
        if people < idx+1:
            cnt += (idx+1) - people
            people += (idx+1) - people
    
    
    print('#{} {}'.format(tc, cnt))