# https://leetcode.com/problems/sum-of-left-leaves/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


############################################################
# 내 풀이 (Stack 을 이용한 DFS)
############################################################
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0

        stack = [(root, False)]
        while stack:
            node, is_left = stack.pop()

            if node.left:
                flag = (node.left, True)
                stack.append(flag)
            if node.right:
                flag = (node.right, False)
                stack.append(flag)
            if not node.left and not node.right and is_left:
                result += node.val
        return result


############################################################
# GPT 풀이 (재귀, DFS)
############################################################
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            if node.left and not node.left.left and not node.left.right:
                left_sum += node.left.val
            return left_sum + right_sum

        return dfs(root)


############################################################
# 다른 사람 풀이 (재귀)
############################################################
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def f(root, isLeft):
            if not root:
                return 0
            if not root.left and not root.right and isLeft:
                return root.val
            return f(root.left, True) + f(root.right, False)

        return f(root, False)
