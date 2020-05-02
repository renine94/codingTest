T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split()) # 수열의 길이, 추가횟수, 출력할 인덱스 번호 L
    arr = list(map(int, input().split()))

    for _ in range(M):
        command = input().split()
        if command[0] == 'I':
            arr.insert(int(command[1]), int(command[2]))
        elif command[0] == 'D':
            arr.pop(int(command[1]))
        else:
            arr[int(command[1])] = int(command[2])
    
    if len(arr) >= L:
        print(f'#{tc} {arr[L]}')
    else:
        print(f'#{tc}', -1)

'''
로직은 저렇게 되는게 맞으나..
Linked_List 로 구현해서 풀어보는걸 권장
'''