# https://www.acmicpc.net/problem/2884

H, M = map(int, input().split())

if M >= 45:
    print(H, M-45)
else:
    M = 60-(45-M)

    if H == 0:
        print(23, M)
    else:
        print(H-1, M)
