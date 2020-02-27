T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 27

    res = []
    i = 1
    while N >= i**3 :
        if N == i**3:
            print('#{} {}'.format(tc, i))
            break
        elif N != i**3:
            i += 1
    else:
        print('#{}'.format(tc), -1)