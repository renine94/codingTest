# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/
# 문제 접근법 해설 도움받았음... 다시 한번 생각해보기 필요

from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        _sum = sum(nums)
        n = len(nums)
        for i in range(n - 1, 1, -1):
            _sum -= nums[i]
            if _sum > nums[i]:
                return _sum + nums[i]
        return -1





# nums, expected = [5, 5, 5], 15
# nums, expected = [1,12,1,2,5,50,3], 12
# nums, expected = [5, 5, 50], -1
# nums, expected = [1,1,2], -1
# nums, expected = [1, 5, 1, 5], 12
# nums, expected = [1, 5, 1, 7], -1
# nums, expected = [1, 5, 1, 8], -1
nums, expected = [1,1,128,8192,16384], -1
# nums, expected = [50,12,2,3,4], 9
result = Solution().largestPerimeter(nums)

assert result == expected