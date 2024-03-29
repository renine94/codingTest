# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

from typing import List
from collections import Counter


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        result = 0
        if max(counter.values()) < k:
            return result

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                subarray = nums[i:j]
                counter = Counter(subarray)
                if max(counter.values()) >= k:
                    result += 1
        return result


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        슬라이딩 윈도우 방식
        """
        result = 0
        left = 0
        max_count = 0
        max_num = max(nums)

        for right, num in enumerate(nums):
            if num == max_num:
                max_count += 1

            while max_count >= k:
                result += len(nums) - right
                if nums[left] == max_num:
                    max_count -= 1
                left += 1

        return result


nums, k, expected = [1, 3, 2, 3, 3], 2, 6
nums, k, expected = (
    [61, 23, 38, 23, 56, 40, 82, 56, 82, 82, 82, 70, 8, 69, 8, 7, 19, 14, 58, 42, 82, 10, 82, 78, 15, 82],
    2,
    224,
)

result = Solution().countSubarrays(nums, k)
assert result == expected, "틀렸는데요"
