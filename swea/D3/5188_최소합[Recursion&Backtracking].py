# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDrI61lYDFAVT#

def find(r, c, s):
    global minV
    if r == N-1 and c == N-1: # 목적지 도착
        if minV > s+m[r][c]:
            minV = s + m[r][c]

    # 백트래킹
    elif minV <= s: # 목적지 도착전에 이미 다른
        return # 이동을 중단하고 다른 경로로

    else:
        if r+1 < N: # 아래로 이동 가능한지 확인
            find(r+1, c, s+m[r][c])
        if c+1 < N: # 오른쪽으로 이동 가능한지 확인
            find(r, c+1, s+m[r][c])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    m = [ list(map(int, input().split())) for _ in range(N) ]

    minV = 100000
    find(0, 0, 0)
    print('#{} {}'.format(tc, minV))
