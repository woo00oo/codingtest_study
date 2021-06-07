def move():
    # 아래, 오른쪽, 위, 왼쪽
    dx = [+1, 0, -1, 0]
    dy = [0, +1, 0, -1]
    dir = 0
    concert_hall[0][0] = 1
    stack = [(0, 0)]
    cur_x = cur_y = 0
    number = 2

    while True:

        while stack:
            cur_x, cur_y = stack.pop()
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            if 0 <= nx < R and 0 <= ny < C:
                if concert_hall[nx][ny] == 0:
                    concert_hall[nx][ny] = number
            else:
                continue

            if number == K:
                return nx + 1, ny + 1
            stack.append((nx, ny))
            number += 1

        stack.append((cur_x, cur_y))

        if dir == 0:
            dir = 1
        elif dir == 1:
            dir = 2
        elif dir == 2:
            dir = 3
        else:
            dir = 0

C, R = map(int, input().split())
K = int(input())
concert_hall = [[0] * (C) for _ in range(R)]

if K > C*R:
    print(0)
else:
    if K == 1:
        print(1, 1)
    else:
        x, y = move()
        print(y, x)

