T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split()) # 노드개수, 리프노드개수, 출력할 노드번호 5 3 2

    tree = [0] * (N+1)
    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value
    # print(tree)

    for i in range(len(tree)-1, 0, -2):
        parent = i//2
        if i % 2:
            tree[parent] = tree[i] + tree[i-1]
        else:
            if i+1 < len(tree):
                tree[parent] = tree[i] + tree[i+1]
            else:
                tree[parent] = tree[i]
    # print(tree)

    result = tree[L]
    # print(result)

    print('#{} {}'.format(tc, result))
