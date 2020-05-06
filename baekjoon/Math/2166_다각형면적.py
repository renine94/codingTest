N = int(input())

x_list = []
y_list = []
for _ in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
x_list.append(x_list[0])
y_list.append(y_list[0])

# print(x_list)
# print(y_list)

result = 0
for i in range(N):
    s = (x_list[i] * y_list[i+1]) - (x_list[i+1] * y_list[i])
    result += s

result = abs(result)/2
result = round(result, 1)
print(result)
