from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.__class__.__name__} val={self.val} left={self.left} right={self.right}>"


############################################################
# 내 풀이 (Stack 을 이용한 DFS)
############################################################
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []

        stack = [(root, str(root.val))]
        while stack:
            node, s = stack.pop()

            if node.left:
                ss = s[:]
                ss += str(node.left.val)
                item = (node.left, ss)
                stack.append(item)
            if node.right:
                ss = s[:]
                ss += str(node.right.val)
                item = (node.right, ss)
                stack.append(item)
            if not node.left and not node.right:
                result.append(int(s))

        return sum(result)


############################################################
# 재귀적 풀이 (GPT)
############################################################
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum = current_sum * 10 + node.val

            if not node.left and not node.right:
                return current_sum

            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)


root, expected = (
    TreeNode(val=1, left=TreeNode(val=2, left=None, right=None), right=TreeNode(val=3, left=None, right=None)),
    25,
)
result = Solution().sumNumbers(root)
assert result == expected
