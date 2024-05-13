# https://leetcode.com/problems/score-after-flipping-matrix/solutions/5150174/easy-to-understand-and-fast-python-solution-beats-90/

from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            rows = grid[i]
            is_convert = len(list(filter(lambda x: x == 0, rows))) > len(list(filter(lambda x: x == 1, rows)))
            if is_convert:
                new_rows = self.convert(rows)
                grid[i] = new_rows

        return grid

    def convert(self, array: list) -> list:
        result = array.copy()
        for i, val in enumerate(array):
            if val == 1:
                result[i] = 0
            else:
                result[i] = 1
        return result


grid = [
    [0, 0, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
]
expected = 39
result = Solution().matrixScore(grid)
assert result == expected


a = b"1111"
int(a, base=0)
