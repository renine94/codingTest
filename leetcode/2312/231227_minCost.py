from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0

        expected_colors = []
        min_ = []
        for i, color in enumerate(colors):
            if not expected_colors:
                expected_colors.append(color)
                min_.append(neededTime[i])
                continue
            elif expected_colors[-1] != color:
                expected_colors.append(color)
                min_.remove(max(min_))
                result += sum(min_)
                min_ = []

            min_.append(neededTime[i])
        
        if min_:
            min_.remove(max(min_))
            result += sum(min_)
        
        return result


# colors, neededTime, expected = 'abaac', [1,2,3,4,5], 3
# colors, neededTime, expected = 'abc', [1,2,3], 0
# colors, neededTime, expected = 'aabaa', [1,2,3,4,1], 2
colors, neededTime, expected = 'aaabbbabbbb', [3,5,10,7,5,3,5,5,4,8,1], 26

result = Solution().minCost(colors, neededTime)

assert result == expected