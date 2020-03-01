import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    string = input()
    sep = ['a', 'e', 'i', 'o', 'u']

    # print(string)

    result = ''
    for s in string:
        if s in sep:
            pass
        else:
            result += s

    print('#{} {}'.format(tc, result))