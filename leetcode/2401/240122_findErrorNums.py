from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        dupe = 0
        n = len(nums)
        correct = n*(n+1) // 2
        wrong = sum(nums)
        diff = correct - wrong

        for idx, _ in enumerate(nums):
            if nums[idx] == nums[idx + 1]:
                dupe = nums[idx]
                break
        return [dupe, dupe + diff]

nums, expected = [1, 2, 2, 4], [2, 3]
# nums, expected = [2, 2], [2, 1]


result = Solution().findErrorNums(nums)
assert result == expected