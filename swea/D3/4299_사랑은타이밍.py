import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    D, H, M = map(int, input().split())
    
    time = (D*24*60 + H*60 + M) - (11*24*60 + 11*60 + 11)
    if time < 0:
        time = -1
    print('#{} {}'.format(tc, time))