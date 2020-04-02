# queue 문제

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    for _ in range(M):
        first = arr.pop(0)
        arr.append(first)
    
    result = arr.pop(0)
    print('#{} {}'.format(tc, result))