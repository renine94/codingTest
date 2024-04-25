# https://leetcode.com/problems/n-th-tribonacci-number/

from functools import lru_cache


#########################################################
# 내 풀이 (재귀) - 시간초과
#########################################################
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n in [1, 2]:
            return 1

        return self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)


#########################################################
# 내 풀이 (재귀) - 최근 입력값 캐싱
#########################################################
class Solution:
    @lru_cache(maxsize=4)
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n in [1, 2]:
            return 1

        return self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)


#########################################################
# 내 풀이 (DP)
#########################################################
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]


n, expected = 4, 4
result = Solution().tribonacci(n)
assert result == expected
