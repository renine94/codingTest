import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    words = input().split()
    sep = ['.', '!', '?']

    # print(words)

    res_list = []
    cnt = 0

    for word in words:
        flag = False

        for idx, w in enumerate(word):
            if idx == 0 and w.isupper():
                flag = True
            
            elif idx !=0 and w.isupper():
                flag = False
            
            elif idx !=0 and w.isnumeric():
                flag = False
        
        if flag :
            cnt += 1
        
        if word[-1] in sep:
            if cnt >= 1:
                res_list.append(cnt)
                cnt = 0
            else:
                res_list.append(0)
    
    print('#{}'.format(tc), *res_list)
