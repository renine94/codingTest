# https://leetcode.com/problems/palindrome-partitioning/

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtrack(s, [], result)
        return result

    def backtrack(self, s, path, result):
        # 문자열을 모두 검사한 경우
        if not s:
            result.append(path[:])
            return

        for i in range(1, len(s) + 1):
            # 부분 문자열이 팰린드롬인지 확인
            if self.is_palindrome(s[:i]):
                # 팰린드롬인 경우, 해당 부분 문자열을 경로에 추가하고 재귀 호출
                path.append(s[:i])
                self.backtrack(s[i:], path, result)
                path.pop()

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
