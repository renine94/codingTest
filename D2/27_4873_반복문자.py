import sys
sys.stdin = open('input.txt')

T=int(input())
for tc in range(1, T+1):
    data = list(input())

    #print(data)

    stack = []
    while len(data) > 0:
        if len(stack) == 0:
            stack.append(data.pop())
            if len(data) == 0:
                break
        
        if stack[-1] == data[-1]:
            data.pop()
            stack.pop()
        
        else:
            stack.append(data.pop())
            if len(data) == 0:
                break
    
    print('#{} {}'.format(tc, len(stack)))