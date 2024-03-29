# https://leetcode.com/problems/sort-characters-by-frequency/

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        sorted_s = sorted(counter.items(), key=lambda x: x[1], reverse=True)

        result = ''
        for c, i in sorted_s:
            for _ in range(i):
                result += c
        return result
    

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        sorted_s = sorted(Counter(s).items(), key=lambda x: x[1], reverse=True)
        return ''.join([c for c, i in sorted_s for _ in range(i)])



s, expected = 'tree', 'eert'
s, expected = "Aabb", "bbAa"
result = Solution().frequencySort(s)

assert result == expected