#문제풀이:
#   node를 방문할때 마다 answer를 1씩 더하면 안됨.

from collections import deque

graph = dict()
N = int(input())
a, b = map(int, input().split())
M = int(input())

for i in range(1, N + 1):
    graph[i] = []

for _ in range(M):
    x, y = map(int, input().split())
    graph[x] = graph[x] + [y]
    graph[y] = graph[y] + [x]


def BFS(start_node, end_node):
    visited = list()
    queue = deque()
    answer = 0
    queue.append(start_node)

    while queue:
        answer += 1
        for _ in range(len(queue)):
            node = queue.popleft()

            if node == end_node:
                return answer - 1

            for i in graph[node]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)
    return -1


print(BFS(a, b))