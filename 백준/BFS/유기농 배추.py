# 배추가 놓여진 위치에서 BFS를 실시
#  BFS를 총 몇회 실시했는지가 이 문제에서 원하는 정답
#   이미 방문한 위치를 표시하기 위해 c라는 2차원리스트에 방문한 위치는 1로 표시
#  2차원 리스트 myMap => myMap[행][열]
#   문제에서 입력시 열,행으로 입력받아 예외가 발생하였다. 주의!!
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = deque()

def BFS(x,y):
    q.append([x,y])
    c[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if myMap[nx][ny] == 1 and c[nx][ny] == 0:
                    c[nx][ny] = 1
                    q.append([nx,ny])

T = int(input())
for _ in range(T):
    M, N, K = list(map(int,input().split()))
    myMap = [[0]*M for _ in range(N)]
    c = [[0]*M for _ in range(N)]
    count = 0
    for _ in range(K):
        y, x = map(int, input().split())
        myMap[x][y] = 1

    for i in range(N):
        for j in range(M):
            if myMap[i][j] == 1 and c[i][j] == 0:
                BFS(i,j)
                count += 1
    print(count)

