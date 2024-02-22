# https://leetcode.com/problems/find-the-town-judge/

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        peoples = [0] * (n + 1)

        for a, b in trust:
            peoples[a] -= 1
            peoples[b] += 1

        for i in range(1, len(peoples)):
            if peoples[i] == n - 1:
                return i
        return -1


n, trust, expected = 3, [[1, 2], [2, 3]], -1
n, trust, expected = 3, [[1, 3], [2, 3], [3, 1]], -1
n, trust, expected = 3, [[1, 3], [2, 3]], 3
result = Solution().findJudge(n, trust)

assert result == expected
