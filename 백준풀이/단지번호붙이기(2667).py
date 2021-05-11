from collections import deque

def BFS(start_x, start_y):
    queue = deque()
    queue.append((start_x,start_y))
    cnt = 1
    visited[start_x][start_y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < N and 0 <= yy < N:
                if myMap[xx][yy] == 1 and visited[xx][yy] == 0:
                    queue.append((xx, yy))
                    cnt += 1
                    visited[xx][yy] = 1
    return cnt


dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]
answer = []
N = int(input())
myMap = [list(map(int,input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if myMap[i][j] == 1 and visited[i][j] == 0:
            answer.append(BFS(i, j))
answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])