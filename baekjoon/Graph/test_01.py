import sys
sys.stdin = open('DFS_input.txt')

def DFS(v): # v 시작지점을 파라미터로 받는다.
    stack = [v]
    visited = []
    while stack:
        current = stack.pop()
        for node in adj_list[current]:
            if not node in visited:
                stack.append(node)
        visited.append(current)
    return visited


node, edge = map(int, input().split())
adj_list = [[] for _ in range(node+1)] # 인덱스 번호 자체가 노드숫자로 하기 위해 +1

# 인접리스트 생성후 값 넣어주기
for _ in range(edge):
    f, t = map(int, input().split())
    adj_list[f].append(t)
    adj_list[t].append(f)
# print('인접리스트 :',adj_list)


visit = DFS(1)

print(visit)





