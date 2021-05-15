# 문제풀이 : 3차원 배열 BFS
# 2차원 배열과 똑같다
# 익은 토마토 1로 부터 BFS를 실시

from collections import deque

dx = [+1, -1, 0, 0, 0, 0]
dy = [0, 0, +1, -1, 0, 0]
dz = [0, 0, 0, 0, +1, -1]


def BFS():
    while queue:
        x, y, z = queue.popleft()
        visited[z][x][y] = 1
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and tomatoes[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                queue.append([nx, ny, nz])
                tomatoes[nz][nx][ny] = tomatoes[z][x][y] + 1
                visited[nz][nx][ny] = 1


M, N, H = map(int, input().split())
tomatoes = []
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
queue = deque()
isTrue = False

for _ in range(H):
    box = [list(map(int, input().split())) for _ in range(N)]
    tomatoes.append(box)

for z in range(H):
    for x in range(N):
        for y in range(M):
            # 익은 토마토의 위치를 모두 큐에다가 넣어준다.
            if tomatoes[z][x][y] == 1:
                queue.append([x, y, z])

BFS()
max_num = 0
for z in range(H):
    for x in range(N):
        for y in range(M):
            # 익지 않은 토마토가 있을 경우 = 즉 모두 익지는 못하는 상황
            if tomatoes[z][x][y] == 0:
                isTrue = True
            # 최소 걸리는 일수 저장
            max_num = max(max_num, tomatoes[z][x][y])
if isTrue:
    print(-1)
else:
    print(max_num - 1)
