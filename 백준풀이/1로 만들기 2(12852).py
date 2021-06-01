from collections import deque

def BFS(node, numbers):
    queue = deque()
    queue.append((node, numbers))

    while queue:
        node, numbers = queue.popleft()

        for num in [node+1, node*2, node*3]:
            if num <= N and visited[num] == 0:
                if num == N:
                    return visited[node] + 1, numbers + [num]
                queue.append((num, numbers + [num]))
                visited[num] = visited[node] + 1


N = int(input())

if N == 1:
    print(0)
    print(1)
else:
    visited = [0] * (N+1)
    cnt, numbers = BFS(1, [1])
    print(cnt)
    print(*numbers[::-1])