from collections import deque
from itertools import combinations

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

def BFS():
    answer = 0
    visited = [[0] * M for _ in range(N)]
    queue = deque(virus)

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        answer += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and myMap[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

    return answer

N, M = map(int, input().split())
myMap = [list(map(int, input().split())) for _ in range(N)]
blank = []
virus = []
wall_len = 0
answer = 0

for i in range(N):
    for j in range(M):
        if myMap[i][j] == 0:
            blank.append((i, j))
        elif myMap[i][j] == 2:
            virus.append((i, j))
        elif myMap[i][j] == 1:
            wall_len += 1

wall = list(combinations(blank, 3))
for i in range(len(wall)):
    for node in wall[i]:
        x, y = node
        myMap[x][y] = 1

    cnt = BFS()
    total = cnt + wall_len + 3

    if answer < M * N - total:
        answer = M * N - total

    for node in wall[i]:
        x, y = node
        myMap[x][y] = 0

print(answer)