from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        
        # If it's not possible to finish all jobs in d days, return -1
        if n < d:
            return -1
        
        # Initialize a 2D array to store the minimum difficulty for each subproblem
        dp = [[float('inf')] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0  # DP[i][k] i개의 작업을 k 일 안에 완료하는데 필요한 최소 어려움의 양
        
        # Iterate through jobs and days to fill the DP array
        for i in range(1, n + 1):
            for k in range(1, d + 1):
                max_difficulty = 0
                for j in range(i, 0, -1):
                    max_difficulty = max(max_difficulty, jobDifficulty[j - 1])
                    dp[i][k] = min(dp[i][k], dp[j - 1][k - 1] + max_difficulty)
        
        return dp[n][d] if dp[n][d] != float('inf') else -1



# jobDifficulty, d, expected
TC = [
    ([186,398,479,206,885,423,805,112,925,656,16,932,740,292,671,360], 4, 1803),
    ([11,111,22,222,33,333,44,444], 6, 843),
    ([6, 5, 4, 3, 2, 1], 2, 7),
    ([9, 9, 9], 4, -1),
    ([1, 1, 1], 3, 3),
]

for jobDifficulty, d, expected in TC:
    result = Solution().minDifficulty(jobDifficulty, d)
    assert result == expected