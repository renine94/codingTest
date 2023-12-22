# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

from collections import Counter


class Solution:
    def maxScore(self, s: str) -> int:
        result = float('-inf')

        for i in range(len(s)):
            left = s[ :i+1]
            right = s[i+1: ]

            l, r = Counter(left), Counter(right)
            sum_ = l.get('0', 0) + r.get('1', 0)

            if sum_ > result:
                result = sum_



s, expected = "011101", 5

result = Solution().maxScore(s)
assert s == expected
