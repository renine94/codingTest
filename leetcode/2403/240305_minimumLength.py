class Solution(object):
    def minimumLength(self, s):
        left, right = 0, len(s) - 1

        while left < right and s[left] == s[right]:
            char = s[left]
            while left <= right and s[left] == char:
                left += 1
            while right >= left and s[right] == char:
                right -= 1

        return right - left + 1


s, expected = "ca", 2
s, expected = "cabaabac", 0
s, expected = "aabccabba", 3
result = Solution().minimumLength(s)

assert result == expected
