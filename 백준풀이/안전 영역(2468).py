from collections import deque

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

def BFS(i, j, rain_height):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and myMap[nx][ny] > rain_height:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))



N = int(input())
myMap = [list(map(int, input().split())) for _ in range(N)]
answer = 1

for rain_height in range(1, 101):
    visited = [[0] * N for _ in range(N)]
    safe = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and myMap[i][j] > rain_height:
                BFS(i, j, rain_height)
                safe += 1

    if safe > answer:
        answer = safe

print(answer)