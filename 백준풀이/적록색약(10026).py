# 첫번째 시도 : 정답
# BFS메소드와 BFS_RG메소드가 비슷하니 하나의 메소드로 리펙토링 해보자.

from collections import deque

def BFS(start_x, start_y, value):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < N and 0 <= new_y < N:
                if visited[new_x][new_y] == 0 and picture[new_x][new_y] == value:
                    visited[new_x][new_y] = 1
                    queue.append((new_x, new_y))

def BFS_RG(start_x, start_y, value):
    queue = deque()
    queue.append((start_x, start_y))
    visited_RG[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < N and 0 <= new_y < N:
                if visited_RG[new_x][new_y] == 0 and picture_RG[new_x][new_y] == value:
                    visited_RG[new_x][new_y] = 1
                    queue.append((new_x, new_y))

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

N = int(input())
picture = []
picture_RG = []
for _ in range(N):
    line = input()
    picture.append(line)
    line = line.replace('R', 'G')
    picture_RG.append(line)

visited = [[0] * N for _ in range(N)]
visited_RG = [[0] * N for _ in range(N)]
answer, answer_RG = 0, 0

# 한번의 2중 포문에서 answer 값과 answer_RG값을 구하려고 2개의 메소드를 구현하였지만 2중 포문을 따로따로 구해줘도 시간초과가 발생하지 않는다.
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS(i, j, picture[i][j])
            answer += 1
        if visited_RG[i][j] == 0:
            BFS_RG(i, j, picture_RG[i][j])
            answer_RG += 1

print(answer, answer_RG)


####### 리펙토링 #############################################

from collections import deque

def BFS(start_x, start_y, value):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < N and 0 <= new_y < N:
                if visited[new_x][new_y] == 0 and picture[new_x][new_y] == value:
                    visited[new_x][new_y] = 1
                    queue.append((new_x, new_y))

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

N = int(input())
picture = []
visited = [[0] * N for _ in range(N)]
answer, answer_RG = 0, 0

for _ in range(N):
    line = input()
    picture.append(line)


for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS(i, j, picture[i][j])
            answer += 1

visited = [[0] * N for _ in range(N)]
for i in range(N):
    picture[i] = picture[i].replace('R', 'G')

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS(i, j, picture[i][j])
            answer_RG += 1

print(answer, answer_RG)