from collections import deque

def BFS(start, end):
    queue = deque()
    distance = [0] * 100001
    visited = [False for _ in range(100001)]
    visited[start] = True
    distance[start] = 0
    queue.append(start)

    while queue:
        node = queue.popleft()
        if 0 <= 2*node <= 100000:
            if not visited[2*node]:
                distance[2*node] = distance[node]
                visited[2*node] = True
                queue.append(2*node)

        if 0 <= node - 1 <= 100000:
            if not visited[node-1]:
                distance[node-1] = distance[node] + 1
                visited[node-1] = True
                queue.append(node-1)
        if 0 <= node + 1 <= 100000:
            if not visited[node+1]:
                distance[node+1] = distance[node] + 1
                visited[node+1] = True
                queue.append(node+1)

    return distance[end]

N, K = map(int, input().split())
print(BFS(N, K))
