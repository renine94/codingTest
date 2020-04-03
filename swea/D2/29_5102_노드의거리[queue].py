def BFS(G, start, goal):
    queue = [start]
    visited = [0] * len(G)
    visited[start] = 1
    while queue:
        node = queue.pop(0)
        if node == goal:
            return visited[node] - 1 # 처음시작위치를 visited[start] = 1 로 시작했기 때문에.
        for n in G[node]:
            if visited[n] == 0:
                queue.append(n)
                visited[n] = visited[node] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        G[n1].append(n2)
        G[n2].append(n1)
    start, goal = map(int, input().split())
    result = BFS(G, start, goal)

    print('#{} {}'.format(tc, result))