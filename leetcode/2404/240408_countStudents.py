from typing import List
from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 샌드위치 0 -> 원형
        # 샌드위치 1 -> 사각형
        students = deque(students)
        sandwiches = deque(sandwiches)
        while students:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
            else:
                students.rotate(-1)

            if len(set(students)) == 1 and students[0] != sandwiches[0]:
                break
        return len(students)


students, sandwiches, expected = [1, 1, 0, 0], [0, 1, 0, 1], 0
# students, sandwiches, expected = [1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1], 3
result = Solution().countStudents(students, sandwiches)

assert result == expected
