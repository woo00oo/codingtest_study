# 문제해결:
#   양방향이 아닌 단방향 그래프를 만들어줌.
#   각 노드에서 BFS를 호출하여 순회한 노드를 구한다.
#   순회한 노드가 많은 것이 문제에서 원하는 정답
#   pypy3로 제출해야 시간초과가 뜨지 않는다.

from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
graph = dict()

for i in range(1,N+1):
    graph[i] = []
for _ in range(M):
    n1, n2 = map(int,sys.stdin.readline().split())
    graph[n2].append(n1)

def BFS(start_node):
    visited = list()
    q = deque()
    q.append(start_node)
    cnt = 1
    while q:
        node = q.popleft()
        if node not in visited:
            visited.append(node)
            q.extend(graph[node])
            cnt += 1
    return cnt

cnt = [-1] * (N +1)
for i in range(1,N+1):
    cnt[i] = BFS(i)
for i in range(len(cnt)):
    if cnt[i] == max(cnt):
        print(i, end = ' ')

