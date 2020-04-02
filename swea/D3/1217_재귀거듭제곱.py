def solution(n, m):
    if m==1:
        return n
    else:
        return solution(n, m-1) * n


T = 10
for tc in range(1, T+1):
    N = int(input())
    A, B = map(int, input().split())
    result = solution(A, B)

    print('#{} {}'.format(tc, result))