# import sys
# sys.stdin = open('input.txt', 'r')
"""
풀이
1. 총점들을 list 에 넣는다.
2. k번째 학생의 index 로 score 를 확인한다.
3. 총점을 정렬시키고 2번에서 찾은 점수로 다시 인덱스를 확인한다.
4. 학점리스트 [D-A] 순으로 만들어서 같은 인덱스 확인
"""


T=int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())
    ts_list = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        t_score = a*0.35 + b*0.45 + c*0.2
        ts_list.append(t_score)

    # 총점 리스트에서 k번째 학생의 점수
    k_score = ts_list[k-1]

    # 정렬된 총점에서 k번째 학생 점수의 index
    ts_list.sort()
    k_index = ts_list.index(k_score)

    # 학생들의 학점 리스트 생성
    grade = [ 'A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0' ]
    cnt = int(n/10)
    grade_list = []
    for i in range(len(grade)):
        for _ in range(cnt):
            grade_list.append( grade[i] )
    # 학점을 D > A 순으로 바꿔준다. ( 왜냐하면 정렬된 총점에서의 k학생점수 인덱스와 같을거니까 )
    r_grade_list = list(reversed(grade_list))

    print('#{} {}'.format(t, r_grade_list[k_index]))