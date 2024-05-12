from typing import List


# 내 풀이
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = n - 2

        result = [[0] * (m) for _ in range(m)]

        for i in range(m):
            for j in range(m):

                max_value = 0
                for x in range(3):
                    for y in range(3):
                        nx = x + i
                        ny = y + j
                        max_value = max(grid[nx][ny], max_value)
                result[i][j] = max_value

        return result


# GPT 에게 최적화 요청 코드
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = n - 2
        result = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(m):
                result[i][j] = max(max(row[j : j + 3]) for row in grid[i : i + 3])

        return result


grid = [
    [9, 9, 8, 1],
    [5, 6, 2, 6],
    [8, 2, 6, 4],
    [6, 2, 2, 2],
]
expected = [
    [9, 9],
    [8, 6],
]
result = Solution().largestLocal(grid)
assert result == expected
