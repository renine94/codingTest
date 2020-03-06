T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 100
    data = ''
    while len(data) != N:
        data += ''.join(input().split())
    
    result = 0
    while str(result) in data:
        result += 1
    
    print('#{} {}'.format(tc, result))