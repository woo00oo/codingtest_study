from collections import deque

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

def BFS(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and myMap[nx][ny] > 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


N, M = map(int, input().split())
myMap = [list(map(int, input().split())) for _ in range(N)]
year = 0

while True:
    visited = [[0] * M for _ in range(N)]
    change_list = []  # 변화된 빙산 정보
    Lump = 0

    # 빙산 덩어리가 2덩어리 이상인가를 BFS를 활용하여 체크
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and myMap[i][j] > 0:
                BFS(i, j)
                Lump += 1

    if Lump >= 2:
        print(year)
        break

    # 1년후에 빙산의 변화
    year += 1

    for x in range(N):
        for y in range(M):
            if myMap[x][y] > 0:
                value = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if myMap[nx][ny] == 0:
                        value += 1
                change_list.append((x, y, value))

    for x, y, value in change_list:
        myMap[x][y] -= value
        if myMap[x][y] < 0:
            myMap[x][y] = 0

    # 빙산이 다 녹았을 때 까지 분리되지 않음
    if len(change_list) == 0:
        print(0)
        break