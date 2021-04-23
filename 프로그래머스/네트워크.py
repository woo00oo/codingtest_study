from collections import deque

def solution(n,computers):
    graph = dict()
    visited = list()
    answer = 0
    for i in range(n):
        graph[i] = list()
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)
    for i in range(n):
        if i not in visited:
            visited = BFS(graph,visited,i)
            answer += 1
    return answer

def BFS(graph,visited,node):
    queue = deque()
    queue.append(node)

    while queue:
        v = queue.popleft()
        if v not in visited:
            queue.extend(graph[v])
            visited.append(v)

    return visited

