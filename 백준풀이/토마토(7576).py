from collections import deque

def BFS():

    while queue:
        start_x, start_y = queue.popleft()
        visited[start_x][start_y] = 1
        for i in range(4):
            x = start_x + dx[i]
            y = start_y + dy[i]

            if 0 <= x < N and 0 <= y < M and tomatoes[x][y] == 0 and visited[x][y] == 0:
                queue.append((x,y))
                tomatoes[x][y] = tomatoes[start_x][start_y] + 1
                visited[x][y] = 1


dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
isTrue = False
queue = deque()

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            queue.append((i, j))
BFS()
answer = 0
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 0:
            isTrue = True
        answer = max(answer, tomatoes[i][j])

if isTrue:
    print(-1)
else:
    print(answer-1)