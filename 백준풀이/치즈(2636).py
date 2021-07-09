from collections import deque

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

def BFS():
    queue = deque()
    queue.append((0, 0))
    visited = [[-1] * M for _ in range(N)]
    visited[0][0] = 0
    cnt = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == -1:
                    if myMap[nx][ny] == 1:
                        myMap[nx][ny] = -1
                        cnt += 1
                    elif myMap[nx][ny] == 0:
                        visited[nx][ny] = 0
                        queue.append((nx, ny))

    return cnt

N, M = map(int, input().split())
myMap = [list(map(int, input().split())) for _ in range(N)]
time = 0
answer = 0
while True:

    cnt = BFS()

    if cnt != 0:
        count = 0
        time += 1
        for i in range(N):
            for j in range(M):
                if myMap[i][j] == -1:
                    myMap[i][j] = 0
                    check = True
                    count += 1
    else:
        break

print(time)
print(count)


