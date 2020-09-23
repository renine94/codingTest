# 입력 데이터
import sys
sys.stdin = open('input.txt')

# 함수 정의
def find_min_cost(start, end, s):
    global minV, N # fcnt
    # fcnt += 1

    # 만약 최대깊이(end)에 도달하고, minV 가 s 보다 크면,
    if start == end:
        if minV > s:
            minV = s # 최대깊이에 도달했을 때의 s (생산비용 모든경우)
        return

	# 백트래킹
    if minV < s: # 최대깊이에 도달하기도 전에 생산비가 minV(최소생산비) 보다 클 경우
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find_min_cost(start + 1, N, s + costs_matrix[start][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 제품 수
    costs_matrix = [ list(map(int, input().split())) for _ in range(N) ]
    visited = [0] * N

    minV = float('inf')
    # fcnt = 0 함수 호출횟수, [백트래킹 사용여부에 따른 호출회수 확인하기 위해서]

    # 함수 실행
    find_min_cost(0, N, 0)

    print(f'#{tc} {minV}')
    # print(f'#{tc} {minV} {fcnt}')
