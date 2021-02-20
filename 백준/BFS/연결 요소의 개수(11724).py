from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
graph = dict()
visited = list()
answer = 0


def BFS(start_node):
    queue = deque()
    queue.append(start_node)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

for i in range(1,N+1):
    graph[i] = list()

for _ in range(M):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    if i not in visited:
        BFS(i)
        answer += 1

print(answer)

