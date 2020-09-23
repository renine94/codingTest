# https://www.acmicpc.net/problem/10869

A, B = map(str, input().split())

lists = ['+', '-', '*', '//', '%']

for item in lists:
    answer = A + item + B
    print(eval(answer))



####### 다른 풀이 #######
A, B = map(int, input().split())

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
