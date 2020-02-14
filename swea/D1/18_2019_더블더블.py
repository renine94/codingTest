"""
1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

주어질 숫자는 30을 넘지 않는다.

[입력]
8

[출력]
1 2 4 8 16 32 64 128 256
"""
N = int(input())

if N <= 30:     
    res = []
    n = 1
    res.append(n)
    for _ in range(N):
        n *= 2
        res.append(n)

    for i in res:
        print(i, end=' ')
else:
    print("1~30까지의 수를 입력해주세요.")    

# a = int(input())
# for i in range(0, a+1):
#     print(2**i,end=' ')


