# 2차원 배열 자료구조를 이용한 BFS 문제.

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def BFS(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    C[start_x][start_y] = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if 0 <= ddx < N and 0 <= ddy < M:
                if my_map[ddx][ddy] == 1 and C[ddx][ddy] == 0:
                    queue.append((ddx, ddy))
                    C[ddx][ddy] = 1


T = int(input())
for _ in range(T):
    M, N, K = map(int,input().split())
    my_map = [[0]*M for _ in range(N)]
    C = [[0]*M for _ in range(N)]
    answer = 0
    for _ in range(K):
        y, x = map(int,input().split())
        my_map[x][y] = 1

    for i in range(N):
        for j in range(M):
            if my_map[i][j] == 1 and C[i][j] == 0:
                BFS(i,j)
                answer += 1
    print(answer)
