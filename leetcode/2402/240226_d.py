# https://leetcode.com/problems/same-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        return False


p = TreeNode(
    val=1,
    left=None,
    right=TreeNode(val=2, left=TreeNode(val=4, left=None, right=TreeNode(val=3, left=None, right=None)), right=None),
)
q = TreeNode(
    val=1,
    left=None,
    right=TreeNode(val=4, left=TreeNode(val=2, left=None, right=TreeNode(val=3, left=None, right=None)), right=None),
)
expected = False


p = TreeNode(val=1, left=TreeNode(val=2, left=None, right=None), right=None)
q = TreeNode(val=1, left=None, right=TreeNode(val=2, left=None, right=None))
expected = False

result = Solution().isSameTree(p, q)

assert expected == result
