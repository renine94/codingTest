from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0

        # 주어진 상태에서 가능한 모든 조합을 생성하는 함수
        def get_next_states(state):
            next_states = []
            for i in range(4):
                digit = int(state[i])
                for direction in [-1, 1]:
                    next_digit = (digit + direction) % 10
                    next_state = state[:i] + str(next_digit) + state[i + 1 :]
                    if next_state not in dead:
                        next_states.append(next_state)
            return next_states

        queue = deque([("0000", 0)])
        visited = set(["0000"])

        # BFS
        while queue:
            state, turns = queue.popleft()
            if state == target:
                return turns
            for next_state in get_next_states(state):
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, turns + 1))

        return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target, expected = "0202", 6

# deadends = ["8888"]
# target, expected = "0009", 1

# deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
# target, expected = "8888", -1

result = Solution().openLock(deadends, target)
assert result == expected
