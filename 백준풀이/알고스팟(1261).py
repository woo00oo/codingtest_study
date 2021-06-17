from collections import deque

def BFS():
    queue = deque()
    distance = [[float('inf')] * M for _ in range(N)]
    queue.append((0, 0))
    distance[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if myMap[nx][ny] == 0:
                    if distance[nx][ny] > distance[x][y]:
                        distance[nx][ny] = distance[x][y]
                        queue.append((nx, ny))
                elif myMap[nx][ny] == 1:
                    if distance[nx][ny] > distance[x][y] + 1:
                        distance[nx][ny] = distance[x][y] + 1
                        queue.append((nx, ny))

    return distance[N-1][M-1]

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

M, N = map(int, input().split())
myMap = [list(map(int, input())) for _ in range(N)]

answer = BFS()
print(answer)