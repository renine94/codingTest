'''
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3
import sys
sys.stdin = open('input.txt')
'''

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    player1 = [0] * 10
    player2 = [0] * 10
    flag = False
    for idx, val in enumerate(cards):
        if idx % 2:
            player2[val] += 1
            for i in range(10):
                if i+2 < 10:
                    if player2[i] == 3 or ( player2[i] >= 1 and player2[i+1] >= 1 and player2[i+2] >= 1 ):
                        print('#{} 2'.format(tc))
                        flag = True
                        break
        else:
            player1[val] += 1
            for i in range(10):
                if i+2 < 10:
                    if player1[i] == 3 or ( player1[i] >= 1 and player1[i+1] >= 1 and player1[i+2] >= 1 ):
                        print('#{} 1'.format(tc))
                        flag = True
                        break
        if flag:
            break
    else:
        print('#{} 0'.format(tc))
