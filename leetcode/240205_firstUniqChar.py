# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         for idx, c in enumerate(s):
#             if s.count(c) == 1:
#                 return idx
#         return -1

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for key, value in counter.items():
            if value == 1:
                return s.index(key)
        return -1


s, expected = 'leetcode', 0
result = Solution().firstUniqChar(s)

assert result == expected