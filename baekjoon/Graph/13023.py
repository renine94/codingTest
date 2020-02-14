# Graph 문제 연습
from pprint import pprint
import sys
sys.stdin = open('input.txt')


# 강사님 풀이

V, Edge = map(int, input().split()) # 노드, 간선
M = [[0] * V for _ in range(V)] # 인접행렬 초기화
#A1 = {node: [] for node in range(V)} # {node : [e1, e2]} 인접리스트 초기화
G = [[] for _ in range(V)] # key 가 숫자로 들어올때, 인접리스트
F = []


for _ in range(Edge):
    f, t = map(int, input().split())
    # 1.인접행렬
    M[f][t] = M[t][f] = 1
    
    
    # 2.인접리스트 ( 배열버전 ) key 가 숫자로 들어올때.
    G[f].append(t) # 양방향
    G[t].append(f)
    
    
    
    # 4. edge 리스트
    F.append([f, t]) # 모든 연결된 간선들의 가능성
    F.append([t, f])
    
    
    for i in range(len(F)):
        for j in range(len(F)):
            A, B = F[i]
            C. D = F[j]
            
            if A == B or A == C or A == D or B == C or B == D or C == D:
                continue
            if not M[B][C]:
                continue
            for E in G[D]:
                if E == A or E == B or E == C or E== D:
                    continue
                print(1)
                sys.exit(0)
                
print(0)



