def solution(board, moves):
    answer = 0
    # board - 격자의 상태가 담긴 2차원 배열
    # moves - 크레인 작동시킨 위치담긴 배열
    # answer - 크레인 모두 작동 후 터트려져 사라진 인형의 개수
    
    basket = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                pass
            else:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        basket.pop()
                        basket.pop()
                        answer += 2
                break
    
    return answer