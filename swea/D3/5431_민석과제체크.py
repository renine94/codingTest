import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # 수강생 수, 제출 인원
    numbers = list(map(int, input().split()))

    # 1 ~ N 까지 번호 생성 ( 수강생 수만큼 )
    list1 = []
    for i in range(1, N+1):
        list1.append(i)

    # 과제 제출 안한사람 번호 res_list 에 담기
    res_list = []
    for num in list1: # 모든 수강생 번호중에서
        if num in numbers:
            pass
        else: # 제출안한친구
            res_list.append(num)


    print('#{}'.format(tc), *sorted(res_list))