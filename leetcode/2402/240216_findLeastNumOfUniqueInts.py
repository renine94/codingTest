from typing import List
from collections import Counter
import collections
import heapq


class Solution:
    # def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    #     counter = dict(Counter(arr))
    #     counter = dict(sorted(counter.items(), key=lambda x: x[1]))

    #     temp = list(counter.keys())
    #     for value in counter.values():
    #         if k >= value:
    #             k -= value
    #             temp.pop(0)
    #     return len(temp)

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        values = list(sorted(Counter(arr).values()))
        while k > 0:
            k -= values.pop(0)
        return len(values) + (k < 0)

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hp = list(collections.Counter(arr).values())
        heapq.heapify(hp)
        while k > 0:
            k -= heapq.heappop(hp)
        return len(hp) + (k < 0)


arr, k, expected = [4, 3, 1, 1, 3, 3, 2], 3, 2
# arr, k, expected = [2,4,1,8,3,5,1,3], 3, 3

result = Solution().findLeastNumOfUniqueInts(arr, k)
assert result == expected
