T = int(input())
for tc in range(1, T+1):
    memory = list(input()) # 메모리의 원래 값 1 <= M <= 50
    # print(memory)

    stack = []
    cnt = 0
    if memory[0] == '1':
        cnt += 1
    for idx in range(len(memory)-1):
        stack.append(memory[idx])
        if stack[-1] != memory[idx+1]:
            cnt += 1
    
    print('#{} {}'.format(tc, cnt))