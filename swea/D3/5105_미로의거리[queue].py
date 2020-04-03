import sys
sys.stdin = open('input.txt')
from pprint import pprint as pp

dx = [-1, 0, 1, 0] # 위, 오른, 아래, 왼
dy = [0, 1, 0, -1]

def BFS(arr, x, y):
    visited = [[0] * len(arr) for _ in range(len(arr))]
    queue = []
    queue.append((x,y))
    while queue:
        x, y = queue.pop(0)
        # x, y 가 찾고자 하는 목표 로직 ( 해야 할 일 )
        if arr[x][y] == 3:
            return visited[x][y]-2 # visited 에다가 거리를 구해놨으므로 -2 만큼해줘야 실제 최단거리가 나온다. (문제 읽어볼 것)
        if visited[x][y] == 0:
            visited[x][y] = 1
            # 인접의 조건 '[상,우,하,좌]' and '벽이아닌곳'
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr):
                if arr[nx][ny] != 1 and visited[nx][ny] == 0: # 벽이 아니고 방문 안했으면
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [ list(map(int, list(input()))) for _ in range(N)]
    # pp(matrix)
    '''
    0 : 통로 
    1 : 벽
    2 : 출발
    3 : 도착
    '''
    # 출발점의 좌표 구하기.
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                start = (i ,j)
                break
    # print(start)
    x, y = start[0], start[1]

    result = BFS(matrix, x, y)

    print('#{} {}'.format(tc, result))