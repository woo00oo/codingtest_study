# 첫번째 풀이 : 성공 but 코드가 복잡하고 지저분하다..

from collections import deque

N, M, x, y, K = map(int, input().split())
myMap = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
x_dice = deque([0, 0, 0, 0])
y_dice = deque([0, 0, 0, 0])

for i in range(K):
    if command[i] == 4:
        if 0 <= x+1 < N:
            number = x_dice.popleft()
            x += 1

            if myMap[x][y] != 0:
                number = myMap[x][y]
                myMap[x][y] = 0
            else:
                myMap[x][y] = number

            x_dice.append(number)
            y_dice[1] = x_dice[1]
            y_dice[3] = x_dice[3]
        else:
            continue

    elif command[i] == 3:
        if 0 <= x-1 < N:
            number = x_dice.pop()
            x -= 1
            x_dice.insert(0, number)
            if myMap[x][y] != 0:
                x_dice[3] = myMap[x][y]
                myMap[x][y] = 0
            else:
                myMap[x][y] = x_dice[3]
            y_dice[1] = x_dice[1]
            y_dice[3] = x_dice[3]
        else:
            continue

    elif command[i] == 1:
        if 0 <= y + 1 < M:
            number = y_dice.popleft()
            y += 1

            if myMap[x][y] != 0:
                number = myMap[x][y]
                myMap[x][y] = 0
            else:
                myMap[x][y] = number

            y_dice.append(number)
            x_dice[1] = y_dice[1]
            x_dice[3] = y_dice[3]
        else:
            continue

    elif command[i] == 2:
        if 0 <= y-1 < M:
            number = y_dice.pop()
            y -= 1
            y_dice.insert(0, number)
            if myMap[x][y] != 0:
                y_dice[3] = myMap[x][y]
                myMap[x][y] = 0
            else:
                myMap[x][y] = y_dice[3]
            x_dice[1] = y_dice[1]
            x_dice[3] = y_dice[3]
        else:
            continue

    print(x_dice[1])

# ------------------------
## 코드 개선
# 주사위를 6개의 면으로 구분 -> dice
# 위 북 동 서 남 아래

import sys

input = sys.stdin.readline
    # 동 서 북 남 순서
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m, x, y, k = map(int, input().split())
myMap = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
dice = [0 for _ in range(6)]

for i in range(k):
    dir = command[i] - 1
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 범위를 벗어나면 아무 행동도 하지 않는다.
    if not 0 <= nx < n or not 0 <= ny < m:
        continue

    if dir == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if myMap[nx][ny] == 0:
        myMap[nx][ny] = dice[5]
    else:
        dice[5] = myMap[nx][ny]
        myMap[nx][ny] = 0

    x, y = nx, ny
    print(dice[0])