from collections import deque
from sys import stdin
input = stdin.readline

def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if my_map[i][j] == 'R':
                rx, ry = i, j
            elif my_map[i][j] == 'B':
                bx, by = i, j
    # R 구슬 위치와 B 구슬 위치, 움직인 횟수를 queue에 저장
    queue.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    cnt = 0

    # 벽을 만나거나 0을 만나기 전까지 계속 직진
    while my_map[x + dx][y + dy] != "#" and my_map[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1

    return x, y, cnt

def bfs():
    init()
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10:
            break
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            if my_map[nbx][nby] != 'O':
                if my_map[nrx][nry] == 'O':
                    print(depth)
                    return
                # R 구술과 B 구술이 같게되면 cnt 값을 비교를 통해 큰 값이 더 늦게 도착했으므로 한칸 뒤로 이동
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, depth+1))
    print(-1)

n, m = map(int, input().split())
my_map = [list(input().rstrip()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
bfs()