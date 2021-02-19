from collections import deque

dw = [1, 1, 0, -1, -1, -1, 0, 1]
dh = [0, 1, 1, 1, 0, -1, -1, -1]

def BFS(myMap,x,y):
    c[x][y] = 1
    queue = deque()

    queue.append([x,y])

    while queue:
        v1, v2 = queue.popleft()
        for i in range(8):
            nx = v1 + dw[i]
            ny = v2 + dh[i]

            if 0 <= nx <= h-1 and 0 <= ny <= w-1:
                if myMap[nx][ny] == 1 and c[nx][ny] == 0:
                    c[nx][ny] = 1
                    queue.append([nx,ny])

while True:
    w, h = map(int,input().split())

    if w == h == 0:
        break

    myMap = [list(map(int,input().split())) for _ in range(h)]
    c = [[0] * w for _ in range(h)]
    answer = 0
    for i in range(h):
        for j in range(w):
            if myMap[i][j] == 1 and c[i][j] == 0:
                BFS(myMap,i,j)
                answer += 1
    print(answer)

