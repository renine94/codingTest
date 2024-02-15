# https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/

from typing import List
from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        w_count = Counter([w for w, l in matches])
        l_count = Counter([l for w, l in matches])

        winners = w_count.keys()
        losers = l_count.keys()

        r1 = list(filter(lambda x: x not in losers, winners))
        r2 = [l for l, c in list(filter(lambda x: x[1] == 1, l_count.items()))]

        r1.sort()
        r2.sort()

        return [r1, r2]



matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
expected = [[1,2,10],[4,5,7,8]]

result = Solution().findWinners(matches)
assert result == expected