from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)

        for i in range(len(dp)-1, -1, -1):
            for j in range(i+1, len(dp)):
                if nums[i]<nums[j]:
                    dp[i]=max(dp[i], 1+dp[j])
        return max(dp)
    


nums, expected = [0, 1, 0, 3, 2, 3], 4
result = Solution().lengthOfLIS(nums)

assert result == expected