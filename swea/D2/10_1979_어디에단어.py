import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    # N**2 행렬 / 단어의 길이 : K
    N, K = map(int, input().split())
    # print(N, K)
    # 2차원 리스트 생성
    # 0 : 검은색 / 1: 흰색 ( 1에 채워야함 )
    matrix = [ list(map(str, input().split())) for _ in range(N) ]
    # pprint(matrix)
    # print('-------------')

    # 가로 검사
    cnt = 0
    for i in range(N):
        for row in ''.join(matrix[i]).split('0'):
            if len(row) == K:
                cnt += 1

        # 세로 검사
        temp = ''
        for j in range(N):
            temp += matrix[j][i] 
        for column in temp.split('0'):
            if len(column) == K:
                cnt += 1
    
    print('#{} {}'.format(t, cnt))

    




