T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int,input().split())
    AB =[A,B]

    # print(AB, C) # 빵가격

    a1, a2 = divmod(C, min(AB))
    # print(a1, a2) # 몫과 나머지

    print('#{} {}'.format(tc, a1))