from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for str in strs:
            counts[tuple(sorted(str))].append(str)
        
        return counts.values()
    

# strs, expected = ["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]
strs, expected = [""], [[""]]
strs, expected = ["a"], [["a"]]
result = Solution().groupAnagrams(strs)

assert list(result) == expected