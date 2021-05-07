# 2차원 배열에서 가로 세로 헷갈려 하지 말기

from collections import deque


def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        n, m = queue.popleft()
        for i in range(4):
            nn = n + dy[i]
            mm = m + dx[i]
            if 0 <= mm < M and 0 <= nn < N:
                if myMap[nn][mm] == 1 and visited[nn][mm] == 0:
                    visited[nn][mm] = 1
                    queue.append((nn, mm))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
T = int(input())
for _ in range(T):
    M, N, K = map(int,input().split())
    myMap = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    answer = 0
    for _ in range(K):
        x, y = map(int, input().split())
        myMap[y][x] = 1
    for i in range(N):
        for j in range(M):
            if myMap[i][j] == 1 and visited[i][j] == 0:
                BFS(i,j)
                answer += 1
    print(answer)




