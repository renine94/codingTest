# 재귀 버전
# def DFS(v):
#     visited[v] = 1

#     print(v, end=' ')

#     for w in G[v]:
#         if not visited[w]:
#             DFS(w)




def DFS(v): # v부터 시작해서 가세요.
    stack = []
    stack.append(v) # 첫번째 방문노드
    visited[v] = 1
    print(v, end="-")

    while stack: # 방금 채운 스택이 없어질때까지.
        p = v
        for w in G[v]:
            if not visited[w]: # 방문안했다면
                stack.append(w) # w로 가시고
                v = w
                visited[w] = 1
                print(v, end="-")
                break
        else:
            if p == v:
                v = stack.pop()

import sys
sys.stdin = open('DFS_input.txt')

V, E = map(int, input().split())

G = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for i in range(E):
    u, v = map(int, input().split()) # u, v 노드와 엣지
    G[u].append(v)
    G[v].append(u)


DFS(1)
