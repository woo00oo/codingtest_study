# BFS 활용

from collections import deque

def BFS(start_x, start_y):
    d = 1
    queue = deque()
    visited = [[0] * M for _ in range(N)]
    queue.append((start_x, start_y))
    visited[start_x][start_y] = d
    while queue:
        d += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if miro[nx][ny] == 1 and visited[nx][ny] == 0:
                        queue.append((nx, ny))
                        visited[nx][ny] = d
    return visited[N-1][M-1]


dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]
N, M = map(int, input().split())
miro = []
for _ in range(N):
    miro.append(list(map(int, input())))
print(BFS(0, 0))