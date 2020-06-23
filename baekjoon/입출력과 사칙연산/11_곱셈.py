# https://www.acmicpc.net/problem/2588

number1 = int(input())
number2 = reversed(list(map(int, list(input()))))

result = 0
for idx, num in enumerate(number2):
    if idx == 0:
        print(number1 * num)
        result += (number1 * num)
    elif idx == 1:
        print(number1 * num)
        result += (number1 * num) * 10
    else:
        print(number1 * num)
        result += (number1 * num) * 100

print(result)




