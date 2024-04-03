#######################################################
# 풀이1
#######################################################
def solution(brown, yellow):
    """
    테두리의 brown 타일 개수와 가운데 yellow 타일 개수가 주어질 때,
    직사각형의 가로 길이와 세로 길이를 반환하는 함수
    """

    # brown 타일 개수와 yellow 타일 개수 사이의 관계식 정의
    def brown_equation(x, y):
        return (2 * x) + (2 * y) - 4

    def yellow_equation(x, y):
        return (x - 2) * (y - 2)

    # 가능한 모든 가로, 세로 길이 조합 탐색
    for x in range(3, brown // 2 + 1):
        for y in range(3, brown // 2 + 1):
            if brown_equation(x, y) == brown and yellow_equation(x, y) == yellow:
                return [y, x]


#######################################################
# 풀이2
#######################################################
def solution(brown, yellow):
    # 전체 타일 개수
    total_tiles = brown + yellow

    # 가로, 세로 길이 후보 탐색
    for y in range(1, total_tiles // 2 + 1):
        x = total_tiles // y
        if total_tiles % y == 0 and x >= y:
            if 2 * x + 2 * y - 4 == brown:
                return [x, y]

    # 유효한 해가 없는 경우
    return []
