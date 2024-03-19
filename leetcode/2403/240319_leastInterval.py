# https://leetcode.com/problems/task-scheduler/description/

from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        print(counter)

        # TODO: 풀이 대기
        pass


tasks, n = ["A", "C", "A", "B", "D", "B"], 1
expected = 6

result = Solution().leastInterval(tasks, n)
assert result == expected
