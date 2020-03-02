import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # N개 시험치고 K개 성적표에 기입
    scores = list(map(int, input().split()))

    result = 0
    for _ in range(K):
        result += scores.pop( scores.index(max(scores)) )
    
    print('#{} {}'.format(tc, result))


