K = int(input())
stack = [] # 포문 안에 쓰면 스택이 자꾸 초기화 되므로 조심
for k in range(1, K+1):
    N = int(input()) # 3 0 4 0

    if N == 0:
        if stack:
            stack.pop()
        else:
            stack = []
    else:
        stack.append(N)
    

print(sum(stack))