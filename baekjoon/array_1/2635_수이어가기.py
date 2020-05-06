D = int(input())

cnt = 0
for i in range(D, D//2, -1):
    temp = [D]
    temp.append(i)

    j = 0
    while True:
        if temp[j] < temp[j+1]:
            break
        else:
            temp.append(temp[j] - temp[j+1])
        j += 1

    if cnt < len(temp):
        cnt = len(temp)
        result = temp

print(cnt)
print(*result)
