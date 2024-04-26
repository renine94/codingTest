from typing import List
import heapq


####################################################################
# DP를 이용한 풀이
####################################################################
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[float("inf")] * n for _ in range(n)]

        # Initialize first row
        dp[0] = grid[0].copy()

        # Fill the dp table
        for i in range(1, n):
            for j in range(n):
                for k in range(n):
                    if k != j:
                        prev = dp[i - 1][k]
                        cur = grid[i][j]
                        dp[i][j] = min(dp[i][j], prev + cur)

        # Find the minimum in the last row
        return min(dp[n - 1])


####################################################################
# Heapq 를 사용한 최적화 풀이
####################################################################
# class Solution:
#     def minFallingPathSum(self, A):
#         for i in range(1, len(A)):
#             r = heapq.nsmallest(2, A[i - 1])
#             for j in range(len(A[0])):
#                 A[i][j] += r[1] if A[i - 1][j] == r[0] else r[0]
#         return min(A[-1])


grid, expected = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
], 13
result = Solution().minFallingPathSum(grid)
print(result == expected)
