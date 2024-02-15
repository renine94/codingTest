from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q, res = deque([root]), 0
        while q:
            node = q.popleft()
            res += node.val if low <= node.val <= high else 0
            if node.val <= high:
                if node.right:
                    q.append(node.right)
            if node.val >= low:
                if node.left:
                    q.append(node.left)
        return res


root = [10,5,15,3,7,13,18,1,None,6]
# TreeNode{val: 10, left: TreeNode{val: 5, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}, right: TreeNode{val: 15, left: None, right: TreeNode{val: 18, left: None, right: None}}}
low, high = 6, 10
expected = 23

result = Solution().rangeSumBST(root, low, high)
assert result == expected