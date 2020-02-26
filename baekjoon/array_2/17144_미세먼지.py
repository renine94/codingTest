from pprint import pprint
from copy import deepcopy

import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

TC= 1
for tc in range(1, TC+1):
    R, C, T = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(R)]
    room2 = deepcopy(room)
    room3 = [i for i in room] # 이것도 deepcopy 효과 낼 수 있따능!!

    for i in range(R):
        for j in range(C):
            if room[i][j] != -1 and room[i][j] != 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C:
                        if room[nx][ny] == -1:
                            pass
                        else:
                            room2[nx][ny] += room[i][j]//5
                            cnt += 1
                room2[i][j] -= ((room[i][j]//5) * cnt)

    # 확산완료! ( deepcopy 시킨거에 적용해야 확산 제대로 됨 )
    pprint(room2)