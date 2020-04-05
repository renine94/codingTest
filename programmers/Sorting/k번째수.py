def solution(array, commands):
    answer = []

    for cmd in commands:
        arr = array[cmd[0]-1: cmd[1]]
        arr.sort()
        res = arr[cmd[2]-1]
        answer.append(res)

    return answer
