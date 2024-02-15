# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']

        half = len(s) // 2
        left = len(list(filter(lambda x: x.lower() in vowels, s[:half])))
        right = len(list(filter(lambda x: x.lower() in vowels, s[half:])))

        return left == right



s, expected = 'book', True
result = Solution().halvesAreAlike()

assert result == expected