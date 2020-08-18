T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    # 전체 점수 합, 평균 구하기
    total = sum(data)
    average = total / N

    # 평균보다 낮은 인원 숫자 세기
    result = 0
    for score in data:
        if score <= average:
            result += 1

    print('#{} {}'.format(tc, result))




