from typing import List
from functools import reduce


#################################################################
# 내 풀이
#################################################################
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        def multiply_elements(nums):
            return reduce(lambda x, y: x * y, nums)

        temps = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                temp = nums[i:j]
                if multiply_elements(temp) < k:
                    temps += 1
        return temps


#################################################################
# 시간초과로 인한 GPT 에게 코드 최적화 요청
#################################################################
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        count = 0
        prod = 1
        left = 0

        for right, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod /= nums[left]
                left += 1
            count += right - left + 1

        return count


nums, k, expected = [10, 5, 2, 6], 100, 8

result = Solution().numSubarrayProductLessThanK(nums, k)
assert result == expected
