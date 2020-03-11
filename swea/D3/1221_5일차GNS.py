from collections import Counter

T = int(input())
for tc in range(1,T+1):
    N = input().split()[1]
    d = input().split()

    a = Counter(d).most_common()
    # print(a)

    cnt_dict = {}
    for num, val in a:
        cnt_dict[num] = val

    # print(cnt_dict)

    char = ["ZRO "*cnt_dict.get('ZRO'), "ONE "*cnt_dict.get('ONE'), "TWO "*cnt_dict.get('TWO'), "THR "*cnt_dict.get('THR'),
            "FOR "*cnt_dict.get('FOR'), "FIV "*cnt_dict.get('FIV'), "SIX "*cnt_dict.get('SIX'),
            "SVN "*cnt_dict.get('SVN'), "EGT "*cnt_dict.get('EGT'), "NIN "*cnt_dict.get('NIN')]
    print('#{}'.format(tc))
    for c in char:
        print(c)