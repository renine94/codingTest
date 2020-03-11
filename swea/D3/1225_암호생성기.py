T = 10
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # print(N)
    # print(numbers)

    i = 1
    while True:
        first = numbers.pop(0)
        end = first - i
        if i == 5:
            i = 0
        if end <= 0:
            end = 0
            numbers.append(end)
            break
        else:
            numbers.append(end)
        i += 1
    
    print(f'#{tc}', *numbers)