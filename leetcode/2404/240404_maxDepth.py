# Stack 사용해서 풀기
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/submissions/1222665319/


######################################################################
# 풀이 1
######################################################################
class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if stack:
                    stack.pop()
                    if not stack:
                        count += 1
        return count


######################################################################
# 풀이 2
######################################################################
class Solution:
    def maxDepth(self, s: str):
        stack = []
        max_depth = 0
        current_depth = 0

        for char in s:
            if char == "(":
                stack.append(char)
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ")":
                if stack:
                    stack.pop()
                    current_depth -= 1
                else:
                    # Invalid parentheses string
                    return -1

        if not stack:
            return max_depth
        else:
            # Invalid parentheses string
            return -1


s, expected = "(1+(2*3)+((8)/4))+1", 3
# s, expected = "(1)+((2))+(((3)))", 3
result = Solution().maxDepth(s)

assert result == expected
