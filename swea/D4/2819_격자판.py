T = int(input())
for tc in range(1, T+1):
    matrix = [list(map(str, input().split())) for _ in range(4) ]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    result = set()
    for i in range(4):
        for j in range(4):
            stack = []
            stack.append((i,j, matrix[i][j]))
            while stack:
                x, y, z = stack.pop()
                if len(z) == 7:
                    result.add(z)
                    continue
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < 4 and 0 <= ny < 4:
                        stack.append((nx, ny, z+matrix[nx][ny]))
            
    print('#{} {}'.format(tc, len(result)))