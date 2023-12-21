from typing import List



class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        sorted_x = sorted(list({x for x, _ in points}))

        result: int = 0
        for i in range(len(sorted_x) - 1):
            diff = sorted_x[i+1] - sorted_x[i]
            if result < diff:
                result = diff
        return result



# points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# expected = 3

points = [[1,5],[1,70],[3,1000],[55,700],[999876789,53],[987853567,12]]
expected = 987853512

result = Solution().maxWidthOfVerticalArea(points)
print(result == expected)
