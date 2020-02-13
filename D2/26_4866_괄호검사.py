# Stack 문제
import sys
sys.stdin = open('input.txt')

T=int(input())
for tc in range(1, T+1):
    data = list(input())
    print(data)

    stack = []
    res = 1
    for d in data:
        if data[0] == ')' or data[0] == '}':
            res = 0
            break
        
        if d == '(' or d == '{':
            stack.append(d)

        elif d == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                elif stack[-1] == '{':
                    res = 0
                    break
            else:
                res = 0
                break
        
        elif d == '}':
            if stack:
                if stack[-1] == '{':
                    stack.pop()
                elif stack[-1] == '(':
                    res = 0
                    break
            else:
                res = 0
                break
    else:
        if stack:
            res = 0

    print('#{} {}'.format(tc, res))



