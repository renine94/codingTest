https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/

from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        tran_grid = list(zip(*grid))

        diff = [[0] * n for _ in range(m)]  # 이렇게 만들어야 리스트안에 리스트들이 서로 다른 객체

        oneRows = [0] * m
        oneCols = [0] * n

        zeroRows = [0] * m
        zeroCols = [0] * n
        
        for i in range(m):
            oneRows[i] = sum(grid[i])
            zeroRows[i] = m - sum(grid[i])
        for j in range(n):
            oneCols[j] = sum(tran_grid[j])
            zeroCols[j] = n - sum(tran_grid[j])
        
        for i in range(m):
            for j in range(n):
                diff[i][j] = oneRows[i] + oneCols[j] - zeroRows[i] - zeroCols[j]
        
        return diff



        
    # def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
    #     m = len(grid) # 가로(행) 길이
    #     n = len(grid[0])  # 세로(열) 길이

    #     diff = [[0] * n for _ in range(m)] # diff matrix 초기화
    #     tranGrid = list(zip(*grid))  # 행렬반전

    #     for i, row in enumerate(grid):
    #         for j, _ in enumerate(row):
    #             oneRow = sum(row)
    #             oneCol = sum(tranGrid[j])
    #             zeroRow = m - oneRow
    #             zeroCol = n - oneCol

    #             diff[i][j] = oneRow + oneCol - zeroRow - zeroCol
        
    #     return diff

grid = [
    # [0, 1, 1],
    # [1, 0, 1],
    # [0, 0, 1]
    [1, 1, 1],
    [1, 1, 1]
]

result = Solution().onesMinusZeros(grid)
expected_result = [
    # [0, 0, 4],
    # [0, 0, 4],
    # [-2, -2, 2],
    [5, 5, 5],
    [5, 5, 5]
]
print(result == expected_result)
