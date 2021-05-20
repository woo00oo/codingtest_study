def DFS(start_node, end_node):
    stack = []
    visited = []
    stack.extend(graph[start_node])

    while stack:
        node = stack.pop()

        if node == end_node:
            return True

        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return False

N = int(input())
graph = dict()
matrix = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N+1):
    graph[i] = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            graph[i+1].append(j+1)

for i in range(N):
    for j in range(N):
        if DFS(i+1, j+1):
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0

for i in range(N):
    print(*matrix[i])
