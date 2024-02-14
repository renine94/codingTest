# https://leetcode.com/problems/rearrange-array-elements-by-sign/

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = [], []
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
        return [item for sublist in list(zip(positive, negative)) for item in sublist]
    

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = [num for num in nums if num > 0] 
        negative = [num for num in nums if num < 0] 
        return [item for sublist in list(zip(positive, negative)) for item in sublist]



nums, expected = [3, 1, -2, -5, 2, -4], [3, -2, 1, -5, 2, -4]
result = Solution().rearrangeArray(nums)

assert result == expected