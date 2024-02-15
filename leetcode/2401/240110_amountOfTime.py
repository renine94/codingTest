from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root.left and not root.right:
            return 0

        # 부모 정보를 포함하여 그래프 생성
        graph = {}
        q = deque([(root, None)])  # 노드와 부모
        while q:
            node, parent = q.popleft()
            if node:
                graph[node.val] = []
                if parent:
                    graph[node.val].append(parent.val)
                if node.left:
                    q.append((node.left, node))
                    graph[node.val].append(node.left.val)
                if node.right:
                    q.append((node.right, node))
                    graph[node.val].append(node.right.val)

        # 그래프를 사용하여 최대 깊이를 찾기 위한 BFS
        visited = set()
        q = deque([(start, 0)])  # 시작 노드와 깊이
        max_depth = 0
        while q:
            node, depth = q.popleft()

            if node not in visited:
                visited.add(node)
                max_depth = max(max_depth, depth)

                for neighbor in graph[node]:
                    q.append((neighbor, depth + 1))

        return max_depth