from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"<TreeNode val={self.val}, left={self.left}, right={self.right}>"


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # 리프노드는 0 or 1 의 값만 가진다.
        if not root.left and not root.right:
            return root.val != 0

        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        if root.val == 2:
            evaluate_root = left or right
        else:
            evaluate_root = left and right

        return evaluate_root


root = TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3, left=TreeNode(val=0), right=TreeNode(val=1)))
result = Solution().evaluateTree(root)
assert result == True
