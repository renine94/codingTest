# https://leetcode.com/problems/leaf-similar-trees/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def DFS(root):
            leafs = []
            stack = [root]
            while stack:
                node = stack.pop()
                if node is None:
                    continue
                if not node.left and not node.right:
                    leafs.append(node.val)
                    continue
                stack.extend([node.right, node.left])
            return leafs
        
        return DFS(root1) == DFS(root2)


# 방법2 (윤호님 풀이)
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        store1 = []
        store2 = []

        def go(node, store):
            if not node:
                return 0
            
            if go(node.left, store) + go(node.right, store) == 0:
                store.append(node.val)
            return 1

        go(root1, store1)
        go(root2, store2)
        return store1 == store2
    

# 방법3 (진영님 풀이)
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def recursive(node):
            if not node:
                return None
            if not node.left and not node.right:
                return node.val

            answer = []
            
            left = recursive(node.left)
            if left:
                if type(left) == list:
                    answer.extend(left)
                else:
                    answer.extend([left])

            right = recursive(node.right)
            if right:
                if type(right) == list:
                    answer.extend(right)
                else:
                    answer.extend([right])
            
            return answer
        
        return recursive(root1) == recursive(root2)