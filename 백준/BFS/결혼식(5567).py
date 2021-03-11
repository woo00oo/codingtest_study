# BFS 수행시 거리가 2인 노드까지만 수행.

from collections import deque


def BFS(start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = True
    level = 0
    cnt = 0

    while queue:
        level += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            for i in graph[node]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
                    cnt += 1
        if level == 2:
            break
    return cnt


n = int(input())
m = int(input())
graph = dict()
visited = [False] * (n+1)
for i in range(1, n + 1):
    graph[i] = []
for _ in range(m):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]
print(BFS(1))
