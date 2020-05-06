x, y = map(int, input().split())
# 가로 세로 길이 리스트.
x_list = [0, x]
y_list = [0, y]

cut = int(input())
for _ in range(cut):
    direction, number = map(int, input().split())
    if direction == 1:  # 세로로 자른다.
        x_list.append(number)
    else:
        y_list.append(number)
x_list.sort()
y_list.sort()

result = 0
square = 0
for i in range(1, len(x_list)):
    for j in range(1, len(y_list)):
        width = x_list[i] - x_list[i-1]
        height = y_list[j] - y_list[j-1]
        square = width * height

        if result < square:
            result = square

print(result)
