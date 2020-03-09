T = 10
for tc in range(1, T+1):
    N = int(input()) # tc번호
    matrix = [ list(input()) for _ in range(100) ]
    # print(matrix)
    matrix_90 = list(map(list, zip(*matrix)))
    # print(matrix_90)

    maxV = 0
    for row in matrix:
        for s in range(100):
            for e in range(99, s, -1):
                if row[s] == row[e]:
                    a = row[s:e+1]
                    b = a[::-1]
                    if a == b:
                        if maxV < len(a):
                            maxV = len(a)
    
    for row in matrix_90:
        for s in range(100):
            for e in range(99, s, -1):
                if row[s] == row[e]:
                    a = row[s:e+1]
                    b = a[::-1]
                    if a == b:
                        if maxV < len(a):
                            maxV = len(a)
    
    print('#{} {}'.format(tc, maxV))