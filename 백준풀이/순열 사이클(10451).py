from collections import deque

def BFS(start_node):
    global  answer
    queue = deque()
    queue.append(start_node)

    while queue:
        node = queue.popleft()

        next_node = graph[node]

        if next_node not in visited:
            queue.append(next_node)
            visited.append(next_node)

    if start_node in visited:
        answer += 1


T = int(input())

for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    graph = dict()
    for i in range(1, N+1):
        graph[i] = numbers[i-1]

    visited = []
    answer = 0

    for node in range(1, N+1):
        if node not in visited:
            BFS(node)

    print(answer)