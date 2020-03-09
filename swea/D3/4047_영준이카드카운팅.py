import sys; sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    S = list(input()) # 카드에 대한 정보 TXY => S01
    # print(S)

    S_cnt = 13
    D_cnt = 13
    H_cnt = 13
    C_cnt = 13

    # S 에서 3개씩 끊어서 알파벳과 숫자 각각 추출
    res_set = set()
    for i in range(0, len(S), 3):
        s = S[i : i+3]
        alpha = s[0]
        number = int(s[1] + s[2])
        # print(alpha, number)

        # 추출한 알파벳과 숫자를 set() 에 넣어줌 ( 중복은 제거 하기 위해서 )
        res_set.add((alpha, number))
    # print(list(res_set))

    # 중복이 제거 되었으면 길이가 4 가 아니기때문에 Error 출력
    if len(list(res_set)) != len(S)//3:
        print('#{} {}'.format(tc, "ERROR"))
    
    # 중복이 없었으면 길이가 4 이므로 아래 작업 수행
    else:
        for alpha, number in list(res_set):
            if alpha == 'S':
                S_cnt -= 1
            if alpha == 'D':
                D_cnt -= 1
            if alpha == 'H':
                H_cnt -= 1
            if alpha == 'C':
                C_cnt -= 1
        
        print('#{} {} {} {} {}'.format(tc, S_cnt, D_cnt, H_cnt, C_cnt))