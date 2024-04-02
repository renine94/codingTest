# https://leetcode.com/problems/isomorphic-strings/submissions/1220742891/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
