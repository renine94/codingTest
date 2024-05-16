from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return root.val != 0

        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        if root.val == 2:
            evaluate_root = left or right
        else:
            evaluate_root = left and right

        return evaluate_root