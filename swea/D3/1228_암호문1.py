import sys
sys.stdin = open('input.txt')

T=10
for tc in range(1, T+1):
    N = int(input()) # 원본 암호문의 길이
    password = input().split()
    M = int(input()) # 명령어의 개수
    command = input().split()

    for idx, cmd in enumerate(command):
        if cmd == 'I':
            p = int(command[idx+1])
            i = int(command[idx+2])

            lst = password[:p]
            lst.extend(command[idx+3 : idx+3+i])
            lst.extend(password[p:])

            password = lst
    
    result = password[:10]

    print('#{}'.format(tc), *result)