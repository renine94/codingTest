T = int(input())

for t in range(1, T+1):
    N = input()
    res = 0
    cnt_list = [0] * 101    # 점수가 0~100 이므로
    score_list = list(map(int, input().split()))

    for score in score_list:
        cnt_list[score] += 1

    for idx, cnt in enumerate(cnt_list):
        if cnt == max(cnt_list):
            res = idx
    

    print('#{} {}'.format(t, res))

    # 문제 링크
    # https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13zo1KAAACFAYh&categoryId=AV13zo1KAAACFAYh&categoryType=CODE
