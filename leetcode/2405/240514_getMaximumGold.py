"""
이 문제를 해결하기 위해서는 백트래킹(backtracking) 알고리즘을 사용해야 합니다.
각 셀에서 시작하여 가능한 모든 경로를 탐색하고, 그 중 최대 금액을 계산해야 합니다. 
아래와 같이 dfs 함수를 작성하여 백트래킹을 구현할 수 있습니다.

위 코드에서 dfs 함수는 다음과 같이 동작합니다:

현재 금액(curr_gold)과 최대 금액(max_gold)을 비교하여 max_gold를 업데이트합니다.
현재 위치에서 4방향(상, 하, 좌, 우)으로 이동할 수 있는지 확인합니다.
이동 가능한 경우, 해당 위치로 이동하고 dfs 함수를 재귀적으로 호출합니다. 이때 curr_gold에 새로운 위치의 금액을 더하고, visited 배열을 업데이트합니다.
재귀 호출이 끝나면 visited 배열을 원래 상태로 되돌립니다.

그리고 getMaximumGold 함수에서는 모든 셀에 대해 dfs 함수를 호출하여 최대 금액을 계산합니다. 초기 visited 배열을 생성하고, 해당 셀에서 dfs 함수를 호출하여 그 셀에서 시작하는 경로의 최대 금액을 구합니다.
이 방식으로 모든 셀에 대해 백트래킹을 수행하면 최종적으로 전체 그리드에서 얻을 수 있는 최대 금액을 구할 수 있습니다.
"""

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_gold = 0

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        # 백트래킹
        def dfs(x, y, curr_gold, visited):
            nonlocal max_gold
            max_gold = max(max_gold, curr_gold)

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    dfs(nx, ny, curr_gold + grid[nx][ny], visited)
                    visited[nx][ny] = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    visited = [[0] * n for _ in range(m)]
                    visited[i][j] = 1
                    dfs(i, j, grid[i][j], visited)

        return max_gold


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_gold = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    visited = [[0] * n for _ in range(m)]
                    visited[i][j] = 1
                    max_gold = max(max_gold, self.dfs(i, j, grid, visited, grid[i][j]))

        return max_gold

    def dfs(self, x, y, grid, visited, curr_gold):
        m, n = len(grid), len(grid[0])
        max_gold = curr_gold

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                max_gold = max(max_gold, self.dfs(nx, ny, grid, visited, curr_gold + grid[nx][ny]))
                visited[nx][ny] = 0

        return max_gold
