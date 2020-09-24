def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if i != j:
                temp = numbers[i] + numbers[j]
                answer.append(temp)

    return sorted(list(set(answer)))
