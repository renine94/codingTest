

T = int(input())
for tc in range(1, T+1):
    m, d = map(int, input().split()) # 1/1 (금)
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = [0, 1, 2, 3, 4, 5, 6] # 월 화 수 목 금 토 일
    # 월 차이
    aa = m-1
    # print(aa)



    if aa > 0:
        total = 0
        for i in range(aa):
            total += days[i]
        total += d
        total = total -1
        if total % 7 == 0:
            print('#{} {}'.format(tc, week[4]))
        elif total % 7 == 1:
            print('#{} {}'.format(tc, week[5]))
        elif total % 7 == 2:
            print('#{} {}'.format(tc, week[6]))
        elif total % 7 == 3:
            print('#{} {}'.format(tc, week[0]))
        elif total % 7 == 4:
            print('#{} {}'.format(tc, week[1]))
        elif total % 7 == 5:
            print('#{} {}'.format(tc, week[2]))
        elif total % 7 == 6:
            print('#{} {}'.format(tc, week[3]))

    else:
        bb = d-1
        if bb % 7 == 0:
            print('#{} {}'.format(tc, week[4]))
        elif bb % 7 == 1:
            print('#{} {}'.format(tc, week[5]))
        elif bb % 7 == 2:
            print('#{} {}'.format(tc, week[6]))
        elif bb % 7 == 3:
            print('#{} {}'.format(tc, week[0]))
        elif bb % 7 == 4:
            print('#{} {}'.format(tc, week[1]))
        elif bb % 7 == 5:
            print('#{} {}'.format(tc, week[2]))
        elif bb % 7 == 6:
            print('#{} {}'.format(tc, week[3]))
    

            
