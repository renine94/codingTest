T = int(input())

input_list = list(map(int, input().split()))
sorted_list = sorted(input_list)
index = int(( T - 1 ) / 2)    # 나누기 연산을 하면 float 로 리턴하기 때문에 다시 int 정수 형변환 필요

print(sorted_list[index])

