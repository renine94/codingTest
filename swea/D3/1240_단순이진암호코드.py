import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 세로, 가로
    matrix = [ list(input()) for _ in range(N) ]
    # print(matrix)

    aaa = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']


    codes = []
    flag = False
    for i in range(N):
        for j in range(1, M+1):
            if matrix[i][-j] == '1':
                end = -j
                codes.extend(matrix[i][end-56+1 : end+1])
                flag = True
                break
        if flag:
            break
    # print(codes, len(codes))

    s = 0
    result = []
    flag = 1
    for idx in range(0, 56, 7):
        temp = ''.join(codes[idx:idx+7])
        tmp = aaa.index(temp)
        result.append(tmp)
        if flag:
            s += tmp*3
            flag = 0
        else:
            s += tmp
            flag = 1

    if s % 10:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, sum(result)))