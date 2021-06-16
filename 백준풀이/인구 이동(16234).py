from collections import deque

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

def BFS(start_x, start_y):
    union = []
    queue = deque()
    union_people_count = myMap[start_x][start_y]
    union.append((start_x, start_y))
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(myMap[nx][ny] - myMap[x][y]) <= R:
                    visited[nx][ny] = 1
                    union.append((nx, ny))
                    union_people_count += myMap[nx][ny]
                    queue.append((nx, ny))

    if len(union) == 1:
        return False

    union_people_count //= len(union)

    for x, y in union:
        myMap[x][y] = union_people_count

    return True

N, L, R = map(int, input().split())
myMap = [list(map(int, input().split())) for _ in range(N)]
answer = 0
while True:
    moved = False
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                if BFS(i, j):
                    moved = True

    if not moved:
        print(answer)
        exit(0)
    else:
        answer += 1