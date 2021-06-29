from collections import deque

def BFS(N, K):
    if N >= K:
        print(N-K)
        print(1)
        return

    dx = [2, 1, -1]
    queue = deque()
    queue.append((N, 0))
    visited = [0 for _ in range(100001)]
    count = 0
    while queue:
        node, cnt = queue.popleft()
        if node == K:
            if not visited[node]:
                visited[node] = cnt
                count += 1
            else:
                if cnt == visited[node]:
                    count += 1

        for i in dx:
            if i == 2:
                new_node = node * i
            else:
                new_node = node + i

            if 0 <= new_node <= 100000:
                if visited[new_node] == 0 or visited[new_node] >= cnt + 1:
                    if visited[K] and cnt + 1 > visited[new_node]:
                        continue
                    visited[new_node] = cnt + 1
                    queue.append((new_node, cnt+1))

    print(visited[K])
    print(count)



N, K = map(int, input().split())
BFS(N, K)