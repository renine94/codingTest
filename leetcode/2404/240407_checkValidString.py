# https://leetcode.com/problems/valid-parenthesis-string/


class Solution:
    def checkValidString(self, s):
        stack = []
        asterisk_stack = []

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == "*":
                asterisk_stack.append(i)
            else:
                if stack:
                    stack.pop()
                elif asterisk_stack:
                    asterisk_stack.pop()
                else:
                    return False

        while stack and asterisk_stack:
            if stack[-1] > asterisk_stack[-1]:
                return False
            stack.pop()
            asterisk_stack.pop()

        return len(stack) == 0
