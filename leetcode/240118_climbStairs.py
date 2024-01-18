# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        """계단 오르는 방법 가지수 구하기"""
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]





n, expected = 1, 1
# n, expected = 2, 2
# n, expected = 3, 3
# n, expected = 7, 21

result = Solution().climbStairs(n)
assert result == expected
