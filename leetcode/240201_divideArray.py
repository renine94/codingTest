from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []

        temp = []
        for num in nums:
            if not temp:
                temp.append(num)
                continue
            
            diff = num - temp[0]
            if diff <= k:
                temp.append(num)
                if len(temp) == 3:
                    result.append(temp)
                    temp = []
            else:
                return []
        
        return result


nums, k, expected = [1, 3, 4, 8, 7, 9, 3, 5, 1], 2, []
nums, k, expected = [1,3,4,8,7,9,3,5,1], 2, [[1, 1, 3]]
nums, k, expected = [1,3,3,2,7,3], 3, []
result = Solution().divideArray(nums, k)

assert result == expected