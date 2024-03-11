# https://leetcode.com/problems/count-elements-with-maximum-frequency/
from typing import List
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        """
        1. 가장 많은 빈도수로 나오는게 몇개인지 구하기
        2. [10,12,11,9,6,19,11] 이라면 11이 2개 나와서 답 2
        3. [1, 2, 3, 4, 5] 각 빈도수가 1이라서 다 더하면 답 5
        4. [1, 2, 2, 3, 4, 4, 5] 2와 4가 2번씩 나와서 답 4
        """
        counter = Counter(nums)
        values = sorted(counter.values(), reverse=True)
        max_val = values[0]
        cnt = values.count(max_val)
        return max_val * cnt
