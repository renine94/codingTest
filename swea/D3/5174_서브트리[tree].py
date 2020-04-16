import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E+1

    data = list(map(int, input().split()))
    # print(data)

    tree = [0 for _ in range(V+1)]
    ch1 = [0 for _ in range(V+1)]
    ch2 = [0 for _ in range(V+1)]

    for i in range(0, len(data), 2):
        parent, child = data[i], data[i+1]
        if ch1[parent] == 0:
            ch1[parent] = child
        else:
            ch2[parent] = child
    # print(ch1)
    # print(ch2)

    count = 0
    def count_it(n):
        global count
        if n == 0:
            return
        count_it(ch1[n])
        count_it(ch2[n])
        count += 1
    count_it(N)
    print(f'#{tc} {count}')



# def find(node, n):
#     global cnt
#     cnt += 1
#     if len(node[n]) == 1:
#         find(node, node[n][0])
#     elif len(node[n]) == 2:
#         find(node, node[n][0])
#         find(node, node[n][1])

# T = int(input())
# for tc in range(1, T+1):
#     e, n = map(int, input().split())
#     node = [[] for _ in range(e+2)]
#     data = list(map(int, input().split()))
#     cnt = 0
#     while data:
#         p = data.pop(0)
#         c = data.pop(0)
#         node[p].append(c)
#     print(node)
#     find(node, n)
#     print(f'#{tc}', cnt)
