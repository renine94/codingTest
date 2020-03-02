import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1, 0, 1, 0] # 위 오른 아래 왼
    dy = [0, 1, 0, -1]

    # res_list = []
    # room_list = []
    max_V = 0 # 최대 이동거리
    min_room_number = 0 # 최소 방의 수

    for r in range(N):
        for c in range(N):
            x = r
            y = c
            cur_room_num = matrix[x][y]
            cnt = 1
            flag = True
            
            while flag: 
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                        if matrix[x][y] +1 == matrix[nx][ny]:
                            x = nx
                            y = ny
                            cnt += 1
                            break
                else:
                    flag = False

        # 각 칸 별로 cnt 비교
            # 더 많이 이동할 때: 무조건 업데이트
            if cnt > max_V:
                max_V = cnt
                min_room_number = cur_room_num
            # 이동 횟수 같을 때: 숫자가 더 작으면 업데이트
            elif cnt == max_V:
                if matrix[r][c] < min_room_number:
                    min_room_number = matrix[r][c]
                    
    # 최종 결과
    print('#{} {} {}'.format(tc, min_room_number, max_V))


    #=================================================================================
    # 리스트로 옮겨 담기 버전

    #         res_list.append(cnt)
    #         room_list.append(cur_room_num)
    
    # idx_list = []
    # for idx, val in enumerate(res_list):
    #     if val == max(res_list):
    #         idx_list.append(idx)
    
    # rooms = []
    # for idx in idx_list:
    #     rooms.append(room_list[idx])

    # result = []
    # result.append(min(rooms))
    # result.append(max(res_list))

    # print('#{}'.format(tc), *result)
