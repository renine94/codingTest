def solution(bridge_length, weight, truck_weights):
    q = [0]*bridge_length  # 다리 길이 만큼 생성하고, 다리위 무게들을 표시
    sec = 0  # 시간 0초부터
    while q:
        sec += 1
        q.pop(0)  # 다리 맨앞쪽 통과
        if truck_weights:  # 트럭줄이 있으면 실행
            if sum(q)+truck_weights[0] <= weight:  # (다리위 무게합 + 줄의첫번째)
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return sec
