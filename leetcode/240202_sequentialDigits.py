from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        queue = list(range(1, 10))

        while queue:
            num = queue.pop(0)

            if low <= num <= high:
                result.append(num)

            last_digit = num % 10
            if last_digit < 9:
                new_num = num * 10 + (last_digit + 1)
                if new_num <= high:
                    queue.append(new_num)

        return result


low, high, expected = 100, 300, [123, 234]
result = Solution().sequentialDigits(low, high)

assert result == expected