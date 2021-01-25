#문제해결:
# 벽이 아닌경우 BFS 수행
# BFS로 벽이 아닐 경우에 이동하면서 늑대나 양의 좌표가 불러와지면 각각 vq와 oq에 저장한다.


from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    c[x][y] = 1
    vq, oq = [], []
    while q:
        x, y = q.popleft()
        if a[x][y] == 'v':
            vq.append([x, y])
        elif a[x][y] == 'o':
            oq.append([x, y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] != '#' and c[nx][ny] == 0:
                    c[nx][ny] = 1
                    q.append([nx, ny])

    # vq, oq의 길이를 비교하여 늑대나 양을 지운다
    if len(vq) >= len(oq):
        for i in oq:
            a[i[0]][i[1]] = '.'
    else:
        for i in vq:
            a[i[0]][i[1]] = '.'

n, m = map(int, input().split())
a = [list(map(str, input().strip())) for _ in range(n)]
c = [[0]*m for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if a[i][j] != '#' and c[i][j] == 0:
            bfs(i, j)


#   늑대와 양의 개수를 새서 출력.
ocnt, vcnt = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 'o':
            ocnt += 1
        elif a[i][j] == 'v':
            vcnt += 1
print(ocnt, vcnt)