# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

from math import ceil
from collections import Counter
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for c in counter.values():
            if c == 1: 
                return -1
            ans += ceil(c / 3)
        return ans
    

# nums, expected = [2,3,3,2,2,4,2,3,4], 4
# nums, expected = [2,1,2,2,3,3], -1
nums, expected = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12], 7

result = Solution().minOperations(nums)

assert result == expected