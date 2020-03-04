def f(n, k, s):
    global maxV # 전역변수 가져다 쓰겠다.
    if s <= maxV: # 백트래킹
        return
    if n == k: 
        if maxV < s:
            maxV = s
    else:
        for i in range(k):
            if used[i] == 0:
                used[i] = 1
                f(n+1, k, s*(P[n][i]/100))
                used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for i in range(N)]
    used = [0] * N
    w = [0] * N
    maxV = 0
    f(0, N, 1)
    print('#{} {:.6f}'.format(tc, maxV*100))