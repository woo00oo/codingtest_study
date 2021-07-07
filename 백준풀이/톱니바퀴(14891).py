from collections import deque
import sys

gear = [deque(list(input())) for _ in range(4)]

K = int(input())
rotate = []
for _ in range(K):
    num, dir = map(int, sys.stdin.readline().split())
    rotate.append((num, dir))

for i in range(K):
    start_gear, start_dir = rotate[i]

    check = [0, 0, 0, 0] # +1 :시계방향, -1: 반시계방향, 0: 회전x
    check[start_gear-1] = start_dir
    # 시작위치가 1번
    if start_gear == 1:
        for idx in range(1, 4):
            if gear[idx-1][2] != gear[idx][6]:
                check[idx] = check[idx-1] * -1

    # 시작위치가 2번
    if start_gear == 2:
        if gear[0][2] != gear[1][6]:
            check[0] = check[1] * -1
        for idx in range(2, 4):
            if gear[idx-1][2] != gear[idx][6]:
                check[idx] = check[idx-1] * -1

    # 시작위치가 3번
    if start_gear == 3:
        if gear[3][6] != gear[2][2]:
            check[3] = check[2] * -1
        for idx in range(1, -1, -1):
            if gear[idx][2] != gear[idx+1][6]:
                check[idx] = check[idx + 1] * -1

    # 시작위치가 4번
    if start_gear == 4:
        for idx in range(2, -1, -1):
            if gear[idx][2] != gear[idx+1][6]:
                check[idx] = check[idx+1] * -1

    # 톱니바퀴 회전
    for idx in range(4):
        if check[idx] == 1:
            gear[idx].rotate(+1)
        elif check[idx] == -1:
            gear[idx].rotate(-1)

answer = 0
score = 1
for i in range(4):
    if gear[i][0] == '1':
        answer += score
    score *= 2

print(answer)