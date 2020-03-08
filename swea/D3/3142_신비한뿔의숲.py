
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 뿔, 동물수 5 3 

    Twin = N-M
    Uni = M-Twin

    print('#{} {} {}'.format(tc, Uni, Twin))
