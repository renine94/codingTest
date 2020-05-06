'''
8
0 1 0 1 0 0 0 1
2
1 3
2 3
'''

Switch = int(input())
Data = ['0']  # 스위치번호 인덱스 맞춰주기 위해 임의로 넣은 더미 데이터
Data.extend(list(map(int, input().split())))
students = int(input())

swap = {1: 0, 0: 1}

for _ in range(students):
    sex, number = map(int, input().split())

    if sex == 1:  # 남학생이면,
        for i in range(1, len(Data)):
            if i % number == 0:  # 자기가 받은수의 배수
                Data[i] = swap[Data[i]]

    else:  # 여학생이면,
        temp = [number - 1, Switch - number]
        i = min(temp)

        while True:
            if Data[number-i] == Data[number+i]:
                D = Data[number-i: number+(i+1)]
                if D == D[::-1]:
                    for j in range(number-i, number+(i+1)):
                        Data[j] = swap[Data[j]]
                    break
            else:
                i -= 1

print(*Data[1:])
