T = 10
for tc in range(1, T+1):
    t = int(input())
    word = list(input())
    data = list(input())

    cnt = 0
    for idx, s in enumerate(data):
        if s == word[0]:
            if data[idx : idx+len(word)] == word:
                cnt += 1

    print("#{} {}".format(t, cnt))