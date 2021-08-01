from collections import deque

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]


def BFS(start_x, start_y, color):
    queue = deque()
    visited = set()
    queue.append((start_x, start_y))
    visited.add((start_x, start_y))


    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 12 and 0 <= ny < 6:
                if (nx, ny) not in visited and myMap[nx][ny] == color:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    return visited


myMap = [list(input()) for _ in range(12)]

answer = 0
while True:
    check = False

    # 1. 뿌요 터트리기
    for i in range(12):
        for j in range(6):
            if myMap[i][j] != '.':
                visited = BFS(i, j, myMap[i][j])
                if len(visited) >= 4:
                    check = True
                    for x, y in visited:
                        myMap[x][y] = '.'

    # 2. 뿌요 내리기
    if check:
        answer += 1

        for j in range(6):
            for i in range(10, -1, -1):
                if myMap[i][j] != '.':
                    for x in range(i+1, 12):
                        if myMap[x][j] == '.':
                            myMap[x][j] = myMap[x-1][j]
                            myMap[x-1][j] = '.'
                        else:
                            break
    else:
        break

print(answer)


