# https://leetcode.com/problems/island-perimeter/
# 육지의 둘레 길이 구하기

from typing import List


###########################################################################
# 내 풀이
###########################################################################
class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # 위, 아래, 왼쪽, 오른쪽
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        result = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    result += 4

                    for r, c in directions:
                        nrow, ncol = row + r, col + c
                        if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
                            if grid[nrow][ncol] == 1:
                                result -= 1
        return result


###########################################################################
# GPT 풀이
###########################################################################
class Solution:
    """
    위 코드를 최적화하려면 여러 가지 방법이 있습니다. 여기서는 중복된 연산을 피하고 불필요한 조건 검사를 줄이는 방법을 사용해 보겠습니다.

    인접한 섬의 개수를 카운트하는 대신에 한 섬의 가장자리만 카운트할 수 있도록 바꿔봅시다. 이를 위해선 각 섬의 가장자리 셀을 찾아야 합니다.
    섬의 가장자리를 찾을 때, 각 셀마다 인접한 네 방향 중에 섬이 아닌 경우에만 가장자리로 판단할 수 있습니다.
    """

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        result = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    result += 4

                    if row > 0 and grid[row - 1][col] == 1:
                        result -= 2
                    if col > 0 and grid[row][col - 1] == 1:
                        result -= 2

        return result


###########################################################################
# GPT 풀이 (DFS 재귀)
###########################################################################
class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            # 방문한 셀은 -1로 표시하여 중복 방문을 방지합니다.
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                return 1
            if grid[row][col] == -1:
                return 0
            grid[row][col] = -1
            perimeter = 0
            perimeter += dfs(row - 1, col)
            perimeter += dfs(row + 1, col)
            perimeter += dfs(row, col - 1)
            perimeter += dfs(row, col + 1)
            return perimeter

        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return dfs(row, col)
