T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))

    if max(data) == min(data):
        print('#{} {}'.format(tc, data[0]))

    elif data.count(max(data)) == 1:
        print('#{} {}'.format(tc, max(data)))

    elif data.count(max(data)) == 2:
        print('#{} {}'.format(tc, min(data)))