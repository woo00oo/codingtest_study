from collections import deque

T = int(input())
vx = [-2,-1,1,2,2,1,-1,-2]
vy = [1,2,2,1,-1,-2,-2,-1]

def BFS(x1,y1,x2,y2):
    answer = 0
    queue = deque()
    queue.append([x1,y1])
    myMap[x1][y1] = 1

    while queue:
        for _ in range(len(queue)):
            nx, ny = queue.popleft()
            if nx == x2 and ny == y2:
                return answer
            for i in range(8):
                rx = nx + vx[i]
                ry = ny + vy[i]
                if 0 <= rx <= N-1 and 0 <= ry <= N-1:
                    if myMap[rx][ry] == 0:
                        queue.append([rx,ry])
                        myMap[rx][ry] = 1
        answer += 1


for _ in range(T):
    N = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    myMap = [[0] * N for _ in range(N)]
    print(BFS(x1,y1,x2,y2))
