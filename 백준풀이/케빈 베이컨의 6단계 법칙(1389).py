# 문제풀이 : 관계를 양방향으로 저장 -> R 딕셔너리
# BFS로 모든 경우에 대해서 구해줌.

from collections import deque

def BFS(node):
    queue = deque()
    queue.append(node)
    c = [-1 for _ in range(N+1)]
    c[node] = 0
    while queue:
        start_node = queue.popleft()
        for i in R[start_node]:
            if c[i] == -1:
                c[i] = c[start_node] + 1
                queue.append(i)
    return sum(c[1:])

N, M = map(int, input().split())
R = dict()
answer = []
res = []
for i in range(1, N+1):
    R[i] = []
for i in range(M):
    p1, p2 = map(int, input().split())
    R[p1].append(p2)
    R[p2].append(p1)

for i in range(1, N+1):
    res.append(BFS(i))

for i in range(N):
    if res[i] == min(res):
        answer.append(i+1)

print(min(answer))


