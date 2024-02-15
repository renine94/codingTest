# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/solutions/4458657/short-code-python-3-cheat-day/

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        주사위 개수 n
        주사위 면수 k
        목표값 target
        """
        MOD = 10**9 + 7

        # dp[주사위 수][숫자의 합]
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):  # 주사위 개수
            for j in range(1, target + 1):  # 목표값
                for num in range(1, k + 1):  # 주사위 면 숫자
                    if j - num >= 0:  # 묙포값 - 주사위면값
                        dp[i][j] = ( dp[i][j] + dp[i - 1][j - num] ) % MOD

        return dp[n][target]
        
# n, k, target = 2, 6, 7
# expected = 6
    
# n, k, target = 1, 6, 3
# expected = 1

n, k, target = 30, 30, 500
expected = 222616187

result = Solution().numRollsToTarget(n, k , target)

assert result == expected