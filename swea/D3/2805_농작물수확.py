T=int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # pprint(arr)

    middle = N//2 # 중간 값..
    res = 0
    for i in range(N):
        dist = abs(middle-i) # 2
        res += sum(arr[i][dist:N-dist])

    print('#{} {}'.format(tc, res))

