T = int(input())

for i in range(1, T+1):
    res = ''
    input_list = list(map(int, input().split()))
    for j in input_list:
        a, b = tuple(input_list)
        if a>b:
            res = '>'
        elif a<b:
            res = '<'
        elif a==b:
            res = '='
    print('#{0} {1}'.format(i, res))
