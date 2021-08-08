# BFS를 활용하여 풀이.

from collections import deque

dx = [-1, -2, -2, -1, +1, +2, +2, +1]
dy = [-2, -1, +1, +2, +2, +1, -1, -2]


def BFS(start_x, start_y, end_x, end_y, l):
    queue = deque()
    visited = [[-1] * l for _ in range(l)]
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 0

    while queue:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            return visited[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


l = int(input())
start_x, start_y = map(int, input().split())
end_x, end_y = map(int, input().split())
answer = BFS(start_x, start_y, end_x, end_y, l)
print(answer)