from typing import List
from collections import defaultdict, deque


###################################################################################################
# 내 풀이 (시간복잡도 O(n^2) 로 타임아웃 발생)
###################################################################################################
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        result = []
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        sorted_items = sorted(graph.items(), key=lambda x: len(x[1]), reverse=True)
        sorted_graph = dict(sorted_items)

        # sorted_graph 를 순회하면서 각 node가 루트노트일 때, 트리의 높이를 result 에 저장한다.
        # 예를들어 result = [(3, 2), (4, 2), (0, 1)] 은 루트노드가 3일때 높이는 2 이다.
        for node in sorted_graph:
            queue = deque([(node, 0)])  # (노드, 높이)
            visited = set()
            max_height = 0

            while queue:
                curr_node, height = queue.popleft()
                visited.add(curr_node)
                max_height = max(max_height, height)

                for neighbor in sorted_graph[curr_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, height + 1))

            result.append((node, max_height))

        # 최소 높이를 가진 노드들만 남기기
        min_height = min(height for _, height in result)
        result = [(node, height) for node, height in result if height == min_height]

        return [node for node, _ in result]


###################################################################################################
# GPT 풀이
###################################################################################################
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # 리프 노드들을 찾기 위해 각 노드의 degree를 계산
        degrees = {node: len(neighbors) for node, neighbors in graph.items()}
        leaves = deque([node for node, degree in degrees.items() if degree == 1])

        # 리프 노드들을 제거하며 최소 높이 트리의 후보들을 찾음
        while n > 2:
            n -= len(leaves)
            new_leaves = deque()
            while leaves:
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        new_leaves.append(neighbor)
            leaves = new_leaves

        return list(leaves)


n, edges, expected = 4, [[1, 0], [1, 2], [1, 3]], [1]
n, edges, expected = 6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]], [3, 4]
result = Solution().findMinHeightTrees(n, edges)
assert result == expected
