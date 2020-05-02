import sys
sys.stdin = open('input.txt')

# 100 x 100 의 0 으로된 행렬 생성 ( 0 ~ 100 까지라고 제약조건 )
matrix = [ [0]*100 for _ in range(100) ]

# 직사각형 넓이만큼 순회하면서 1 로 만들어줌 ( 겹쳐도 1 로 만듬 )
for _ in range(4):
    num = list(map(int, input().split()))
    for r in range(num[0], num[2]):
        for c in range(num[1], num[3]):
            matrix[r][c] = 1

# 각 matrix의 row들 다 합쳐서 계산
result = 0
for row in matrix:
    res = sum(row)
    result += res
print(result)
