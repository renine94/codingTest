# https://leetcode.com/problems/find-all-groups-of-farmland/

from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        result = []
        rows, cols = len(land), len(land[0])

        visited = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if land[row][col] == 1 and not visited[row][col]:
                    top_left = [row, col]
                    bottom_right = [row, col]
                    stack = [(row, col)]
                    visited[row][col] = 1

                    while stack:
                        cur_row, cur_col = stack.pop()

                        top_left[0] = min(top_left[0], cur_row)
                        top_left[1] = min(top_left[1], cur_col)
                        bottom_right[0] = max(bottom_right[0], cur_row)
                        bottom_right[1] = max(bottom_right[1], cur_col)

                        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            new_row, new_col = cur_row + dr, cur_col + dc
                            if (
                                0 <= new_row < rows
                                and 0 <= new_col < cols
                                and land[new_row][new_col] == 1
                                and not visited[new_row][new_col]
                            ):
                                stack.append((new_row, new_col))
                                visited[new_row][new_col] = 1
                    result.append(top_left + bottom_right)

        return result
