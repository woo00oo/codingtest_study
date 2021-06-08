# 1차 풀이 : 시간초과
# 브루트포스 + BFS 활용
# 모든 벽을 한번씩 제거후에 BFS실시 후 최단 경로 찾기

from collections import deque
import sys

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

def BFS():
    visited = [[0] * M for _ in range(N)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and myMap[nx][ny] == '0':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    if visited[-1][-1] == 0:
        return 1e9
    return visited[-1][-1]


N, M = map(int, input().split())
myMap = [list(sys.stdin.readline().strip()) for _ in range(N)]
wall = []
answer = 1e9

for i in range(N):
    for j in range(M):
        if myMap[i][j] == '1':
            wall.append((i, j))

for node in wall:
    x, y = node
    myMap[x][y] = '0'
    distance = BFS()
    myMap[x][y] = '1'
    if answer > distance:
        answer = distance

if answer == 1e9:
    print(-1)
else:
    print(answer)

## --------------------------------------------------------

# 3차원 배열을 만들어 세번째 차수에는 벽을 뚫었는지 여부를 저장한다.
# 벽이 아닌 경우 일반적인 BFS를 수행한다.
# 벽이고 그 벽을 뚫은 적이 없는 경우 세번째 차수 값을 수정하여 큐에 넣어준다.(벽을 한번 뚫을수 있고 세번째 차수를 +1를 해줘 더 이상 벽을 뚫을 수 없게 설정)
# 결과적으로 한번의 BFS 수행으로 벽을 한 개 까지 부쉈을 때 최단 거리를 구할 수 있다.

# [x][y][0] 칸은 벽을 아직 한번도 부순적이 없을 때의 최단 경로 횟수가 들어가 있음
# [x][y][1] 칸은 벽을 이미 한번 부수고 왔을 때의 최단 경로

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS():
    queue = deque()
    queue.append([0, 0, 0])
    visited[0][0][0] = 1
    while queue:
        x, y, z = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if myMap[nx][ny] == 0 and visited[nx][ny][z] == -1:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append([nx, ny, z])
                # 벽을 한번 부실 수 있음.
                elif z == 0 and myMap[nx][ny] == 1 and visited[nx][ny][z+1] == -1:
                    visited[nx][ny][z+1] = visited[x][y][z] + 1
                    queue.append([nx, ny, z+1])

n, m = map(int, input().split())
myMap = [list(map(int, input())) for _ in range(n)]
visited = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
BFS()
# ans1은 벽을 한번도 뚫지 않고 왔을 때의 최단 경로,
# ans2은 벽을 한번 뚫고 왔을 때의 최단 경로
ans1, ans2 = visited[n-1][m-1][0], visited[n-1][m-1][1]
if ans1 == -1 and ans2 != -1:
    print(ans2)
elif ans1 != -1 and ans2 == -1:
    print(ans1)
else:
    print(min(ans1, ans2))
