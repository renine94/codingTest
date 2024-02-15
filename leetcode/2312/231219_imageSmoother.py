from typing import List
import math

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])

        diff = [[0] * n for _ in range(m)]

        left_up = (-1, -1)
        left = (0, -1)
        left_down = (1, -1)
        current = (0, 0)
        current_up = (-1, 0)
        current_down = (1, 0)
        right_up = (-1, 1)
        right = (0, 1)
        right_down = (1, 1)

        check_lists = [left_up, left, left_down, current, current_up, current_down, right_up, right, right_down]
        for x in range(m):
            for y in range(n):
                temp = 0
                count = 0
                for x_, y_ in check_lists:
                    nx, ny = x + x_, y + y_
                    if 0 <= nx < m and 0 <= ny < n:
                        temp += img[nx][ny]
                        count += 1
                diff[x][y] = math.floor(temp / count)
        return diff
                
img = [
    [100, 200, 100],
    [200, 50, 200],
    [100, 200, 100]
]
result = Solution().imageSmoother(img)
expected = [
    [137, 141, 137],
    [141, 138, 141],
    [137, 141, 137]
]
print(result == expected)