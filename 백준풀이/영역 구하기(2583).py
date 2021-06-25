from collections import deque

def BFS(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if myMap[nx][ny] == 0 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1

    area.append(cnt)

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

M, N, K = map(int, input().split())
myMap = [[0] * N for _ in range(M)]
area = []

# 사각형 영역 -> 1로 변환
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            myMap[i][j] = 1

# BFS를 통해 영역 체크
visited = [[0]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if myMap[i][j] == 0 and visited[i][j] == 0:
            BFS(i, j)

area.sort()
print(len(area))
print(*area)
