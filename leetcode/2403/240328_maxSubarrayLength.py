from typing import List
from collections import Counter


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        def is_good_subarray(array: list):
            counter = Counter(array)
            values = counter.values()
            if min(values) != max(values) or max(values) > k:
                return False

            return True

        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                subarray = nums[i:j]
                length = len(subarray)

                if is_good_subarray(subarray):
                    if result < length:
                        result = length

        return result


nums, k, expected = [1, 2, 3, 1, 2, 3, 1, 2], 2, 6
nums, k, expected = [1, 1, 2], 2, 3
result = Solution().maxSubarrayLength(nums, k)

assert result == expected
