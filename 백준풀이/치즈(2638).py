# 문제풀이 :
#   BFS()를 통해 인접한 칸이 치즈면(myMap[nx][ny] >= 1) 값을 1 증가하고
#   치즈가 없으면(myMap[nx][ny]==0) 방문을 확인해주고 이동.

from collections import deque

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

def BFS():
    queue = deque()
    queue.append((0, 0))
    visited = [[-1] * M for _ in range(N)]
    visited[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == -1:
                    if myMap[nx][ny] >= 1:
                        myMap[nx][ny] += 1
                    else:
                        visited[nx][ny] = 0
                        queue.append((nx, ny))

N, M = map(int, input().split())
myMap = [list(map(int, input().split())) for _ in range(N)]
time = 0

while True:
    BFS()
    check = False

    for i in range(N):
        for j in range(M):
            # 3이상인 것은(외부 공기가 2개 이상인것으로 0으로 바꿔줌
            if myMap[i][j] >= 3:
                myMap[i][j] = 0
                check = True
            # 2인 것은 인접한 칸에 공기가 1개인 것이니 다시 1로 바꿔줌(녹지 않고 치즈 유지)
            elif myMap[i][j] == 2:
                myMap[i][j] = 1
    # 치즈가 녹은게 있으면 시간 증가
    if check:
        time += 1
    # 더 이상 녹은 치즈가 없다면 (모두) 녹았다면 종료
    else:
        break

print(time)