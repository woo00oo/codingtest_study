# 물이 차있을 예정인 곳은 이동하지 못하므로 물을 먼저 이동시키고 고슴도치를 이동 하는 순
# 고슴도치가 이동할 수 있는 모든 경우의 수를 반복해야 하기 때문에 qlen 동안 while문 처리

from collections import deque

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

def BFS(S_x, S_y, D_x, D_y):
    queue = deque()
    queue.append((S_x, S_y))
    visited[S_x][S_y] = 0

    while queue:
        new_water = []
        while water:
            x, y = water.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < R and 0 <= ny < C:
                    if myMap[nx][ny] == '.':
                        myMap[nx][ny] = '*'
                        new_water.append((nx, ny))
        water.extend(new_water)

        qlen = len(queue)
        while qlen:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if visited[nx][ny] == -1:
                        if myMap[nx][ny] == '.':
                            visited[nx][ny] = visited[x][y] + 1
                            queue.append((nx, ny))
                        elif myMap[nx][ny] == 'D':
                            visited[nx][ny] = visited[x][y] + 1
                            return visited[nx][ny]
            qlen -= 1

    return "KAKTUS"

R, C = map(int, input().split())
myMap = [list(input()) for _ in range(R)]
S_x, S_y = 0, 0
D_x, D_y = 0, 0
water = []
visited = [[-1] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if myMap[i][j] == 'S':
            S_x, S_y = i, j
        elif myMap[i][j] == 'D':
            D_x, D_y = i, j
        elif myMap[i][j] == '*':
            water.append((i, j))

print(BFS(S_x, S_y, D_x, D_y))

