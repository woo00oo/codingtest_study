from collections import deque

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

def BFS():
    queue = deque()
    visited = [[-1] * N for _ in range(N)]
    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1 and my_map[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return visited[-1][-1]


N = int(input())
my_map = [list(map(int, input().split())) for _ in range(N)]
answer = BFS()

if answer == -1:
    exit(0)
else:
    print(answer)
