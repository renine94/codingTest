# https://leetcode.com/problems/unique-number-of-occurrences/description/

from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        cnt = counter.values()
        before = len(cnt)
        after = len(set(cnt))
        return before == after


arr = [1,2,2,1,1,3]
expected = True

result = Solution().uniqueOccurrences(arr)
assert result == expected