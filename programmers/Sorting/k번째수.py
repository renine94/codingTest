def solution(array, commands):
    answer = []

    for cmd in commands:
        arr = array[cmd[0]-1: cmd[1]]
        arr.sort()
        res = arr[cmd[2]-1]
        answer.append(res)

    return answer


def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        target = array[i-1: j]
        sorted_target = sorted(target)
        answer.append(sorted_target[k-1])
    return answer