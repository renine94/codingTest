from typing import List
from collections import defaultdict


#############################################################################################
# 내 풀이
#############################################################################################
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True

        nodes = defaultdict(list)
        visited = [0] * n

        for edge in edges:
            start, end = edge
            nodes[start].append(end)
            nodes[end].append(start)

        stack = [source]
        while stack:
            node = stack.pop()
            next_nodes = nodes[node]
            if destination in next_nodes:
                return True
            else:
                if not visited[node]:
                    visited[node] = 1
                    stack.extend(next_nodes)
        return False


#############################################################################################
# 내 풀이를 GPT 에게 최적화 요청한 코드
# 인접 리스트 대신 집합을 사용하여 중복 엣지를 제거하고 인접한 노드 확인 시간을 O(1)로 단축합니다.
# 비트 마스크를 사용하여 방문한 노드를 추적하고 메모리 사용량을 줄입니다.
# 스택 대신 재귀 호출을 사용하여 코드를 간결하게 만듭니다.
#############################################################################################
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True

        graph = {node: set() for node in range(n)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        visited = 0

        def dfs(node):
            nonlocal visited
            if node == destination:
                return True
            visited |= 1 << node
            for neighbor in graph[node]:
                if visited & (1 << neighbor) == 0:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(source)


n = 3
edges = [
    [0, 1],
    [1, 2],
    [2, 0],
]
source = 0
destination = 2

# n = 5
# edges = [
#     [0, 4],
# ]
# source = 0
# destination = 4

n = 6
edges = [
    [0, 1],
    [0, 2],
    [3, 5],
    [5, 4],
    [4, 3],
]
source = 0
destination = 5

result = Solution().validPath(n, edges, source, destination)
assert result == True
