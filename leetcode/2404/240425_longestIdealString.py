# https://leetcode.com/problems/longest-ideal-subsequence/
# 못 풀었음 DP 사용해야되는것 같은데,, 아직 정답 못봐서 모름,,,

import string


# 내 풀이
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        distance = {char: i for i, char in enumerate(string.ascii_lowercase, 1)}

        result = float("-inf")

        for i in range(len(s)):
            ss = s[i]
            for j in range(i + 1, len(s)):
                char = s[j]
                diff = abs(distance[ss[-1]] - distance[char])
                if diff <= k:
                    ss += char
            result = max(result, len(ss))
        return result


s, k, expected = "acfgbd", 2, 4
s, k, expected = "pvjcci", 4, 2
s, k, expected = "eduktdb", 15, 5
result = Solution().longestIdealString(s, k)
assert expected == result
