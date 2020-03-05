T = int(input())
for tc in range(1, T+1):
    L, U, X = map(int, input().split())

    result = 0
    if L <= X <= U:
        result = 0
    
    elif X < L:
        result = L - X
    
    elif X > U:
        result = -1

    
    print('#{} {}'.format(tc, result))