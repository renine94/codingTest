from typing import List

############################################################################
# 내 풀이
############################################################################


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_ = min(nums)
        if min_ != 1 and 1 not in nums:
            return 1

        while True:
            min_ += 1
            if min_ <= 0:
                continue
            if min_ not in nums:
                return min_


############################################################################
# GPT 최적화 요청
############################################################################


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_ = 1
        while min_ in nums:
            min_ += 1
        return min_


############################################################################
# GPT 최적화 요청 (시간초과 해결)
############################################################################


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        min_positive = 1

        # List 보다 Set 이 조회성능이 O(1) 로 좋다. HashMap 자료구조를 사용하기 때문
        while min_positive in nums_set:
            min_positive += 1

        return min_positive


nums, expected = [1, 2, 0], 3

result = Solution().firstMissingPositive(nums)

assert result == expected
