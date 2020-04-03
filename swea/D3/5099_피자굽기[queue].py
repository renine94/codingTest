T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 화덕크기, 피자 개수
    cheezes = list(map(int, input().split()))

    # queue 생성
    fire = [] # 화덕통
    idx = 1 # 피자번호
    for _ in range(N):
        fire.append([idx, cheezes.pop(0)])
        idx += 1
        
    while True:
        fire[0][1] //= 2
        if fire[0][1] == 0:
            fire.pop(0)
            if cheezes:
                fire.append( [idx,cheezes.pop(0)] )
                idx += 1
        else:
            first = fire.pop(0)
            fire.append(first)
        if len(fire) == 1:
            break
    result = fire[0][0]
    print(f'#{tc} {result}')