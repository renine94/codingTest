import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    string = list(input())
    H = int(input())
    place = sorted(map(int, input().split()), reverse=True)
    # print(string, H, place)

    # place 를 내림차순으로 인덱스 뒤쪽부터 추가시키면 앞에 인덱스에 영향 없음
    for p in place:
        string.insert(p, '-')
    
    # print(string)
    
    result = ''
    for s in string:
        result += s

    print('#{} {}'.format(tc, result))
