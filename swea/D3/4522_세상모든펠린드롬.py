T = int(input())
for tc in range(1, T+1):
    string = list(input())
    flag = True

    for i in range(len(string)):
        if string[i] == '?':
            continue
        if string[len(string)-1-i] == '?':
            continue
        if string[i] != string[len(string)-1-i]:
            flag = False

    if flag:
        print('#{} {}'.format(tc, "Exist"))
    else:
        print('#{} {}'.format(tc, "Not exist"))
