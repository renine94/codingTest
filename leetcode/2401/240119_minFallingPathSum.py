from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        # 두 번째 마지막 행에서 첫 번째 행까지 역순으로 반복
        for i in range(rows - 2, -1, -1):
            for j in range(cols):
                # 현재 위치의 최소 경로 합 계산
                matrix[i][j] += min(
                    matrix[i + 1][j],
                    matrix[i + 1][max(0, j - 1)],
                    matrix[i + 1][min(cols - 1, j + 1)]
                )

        # 최소 경로 합은 첫 번째 행의 최소값
        return min(matrix[0])







matrix, expected = [[2,1,3],[6,5,4],[7,8,9]], 13
matrix, expected = [
    [-80,-13,22],
    [83,94,-5],
    [73,-48,61]
], -66



result = Solution().minFallingPathSum(matrix)
assert result == expected