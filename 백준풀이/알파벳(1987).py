# BFS + 백트래킹
# 일반 BFS와 달리 큐에 x, y축과 지나온 경로를 append 시킨다.
# 그 경로를 통하여 알파벳 중복 확인과 최대 경로를 구해줄 수 있다.

from collections import deque
import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def BFS(x, y):
    global answer
    queue = deque([(x, y, board[x][y])])

    while queue:
        x, y, ans = queue.popleft()

        # 좌우상하 갈 수 있는지 살펴본다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in ans:
                queue.append((nx, ny, ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

answer = 1
BFS(0, 0)
print(answer)