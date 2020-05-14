# 분할정복 / 이진트리
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
# 5207. 이진탐색
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 데이터 입력
    N, M = map(int, input().split())
    A = list(sorted(map(int, input().split()))) # len(A) == N , 정렬한 상태로 A 에 저장한다....
    B = list(map(int, input().split())) # len(B) == M
    result = 0

    # 로직 구현
    for num in B:
        if num in A :
            l = 0
            r = len(A) - 1
            m = (l + r) // 2
            flag = 2 # 방향

            while True :
                if A[m] == num:
                    result +=1
                    break

                if A[m] < num :
                    l = m + 1
                    m = (l + r) // 2
                    if flag == 0 or flag == 2:
                        flag = 1 # 오른쪽
                    else:
                        break

                elif A[m] > num :
                    r = m - 1
                    m = (l + r) // 2
                    if flag == 1 or flag == 2:
                        flag = 0 # 왼쪽
                    else:
                        break

        else:
            continue

    print(f'#{tc} {result}')

######## 재귀 풀이 ##########
def go(n, l, r, v):
    global res
    while True:
        m = (l + r) // 2
        if n == nums1[m]:
            res += 1
            return
        if l == r:
            return
        if n > nums1[m]:
            if v != 1:
                l, v = m+1, 1
                continue
        else:
            if v != -1:
                r, v = m-1, -1
                continue
        return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums1 = sorted(list(map(int, input().split())))
    nums2 = list(map(int, input().split()))
    res = 0
    for n in nums2:
        go(n, 0, N-1, 0)
    print(f'#{tc} {res}')
