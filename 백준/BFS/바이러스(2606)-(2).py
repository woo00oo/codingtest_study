# 딕셔너리 자료구조를 사용한 BFS 문제.

from collections import deque

def BFS(start_node):
    visited = list()
    queue = deque()
    queue.append(start_node)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return len(visited) - 1

N = int(input())
G = int(input())
graph = dict()

for i in range(1,N+1):
    graph[i] = []
for _ in range(G):
    N1, N2 = map(int,input().split())
    graph[N1] = graph[N1] + [N2]
    graph[N2] = graph[N2] + [N1]

print(BFS(1))