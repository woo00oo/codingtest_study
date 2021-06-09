from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y, weight, time, eat):
    q, can_eat = deque(), []
    q.append([x, y])
    visited = [[-1]*n for _ in range(n)]
    visited[x][y] = time
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if visited[nx][ny] == -1:
                        if myMap[nx][ny] == 0 or myMap[nx][ny] == weight:
                            visited[nx][ny] = visited[x][y] + 1
                            q.append([nx, ny])
                        elif 0 < myMap[nx][ny] < weight:
                            can_eat.append([nx, ny])
            qlen -= 1

        if can_eat:
            nx, ny = min(can_eat)
            eat += 1
            if eat == weight:
                eat = 0
                weight += 1
            myMap[nx][ny] = 0
            return nx, ny, weight, visited[x][y] + 1, eat

    print(time)
    sys.exit()

n = int(input())
myMap = [list(map(int, input().split())) for _ in range(n)]
x, y = 0, 0
for i in range(n):
    for j in range(n):
        if myMap[i][j] == 9:
            x, y = i, j
            myMap[i][j] = 0

weight, time, eat = 2, 0, 0
while True:
    x, y, weight, time, eat = bfs(x, y, weight, time, eat)