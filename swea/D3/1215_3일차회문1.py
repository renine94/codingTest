T = 10
for tc in range(1, T+1):
    N = int(input()) # 찾아야 하는 길이
    matrix = [ list(input()) for _ in range(8) ]
    # print(matrix)
    matrix_90 = list(map(list, zip(*matrix)))
    # print(matrix_90)

    cnt = 0
    for row in matrix:
        for i in range(8-N+1):
            a = row[i:i+N]
            b = a[::-1]
            if a == b:
                cnt += 1
    
    for row in matrix_90:
        for i in range(8-N+1):
            a = row[i:i+N]
            b = a[::-1]
            if a == b:
                cnt += 1

    print('#{} {}'.format(tc, cnt))