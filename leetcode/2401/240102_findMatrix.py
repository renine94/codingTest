# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/solutions/4490217/hash-table-solution-beats-87-in-speed/

from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        temp = []
        while nums:
            for num in nums:
                if num not in temp:
                    temp.append(num)

            for n in temp:
                nums.remove(n)
            result.append(temp)
            temp = []
        
        return result



nums = [1, 3, 4, 1, 2, 3, 1]
expected = [[1, 3, 4, 2], [1, 3], [1]]
result = Solution().findMatrix(nums)
        
assert result == expected