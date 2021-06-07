import sys
from collections import deque

R, C, N = map(int, sys.stdin.readline().split())
myMap = [list(sys.stdin.readline().strip()) for _ in range(R)]
dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]
time = 1
bombs = deque()
while True:

    time += 1 # 1초 증가

    # 모든 칸에 폭탄 설치
    for i in range(R):
        for j in range(C):
            if myMap[i][j] == 'O':
                bombs.append((i, j))
            elif myMap[i][j] == '.':
                myMap[i][j] = 'O'

    if time == N:
        break

    time += 1 # 1초 증가

    # 3초 전에 설치된 폭탄 모두 폭발
    while bombs:
        r, c = bombs.popleft()
        myMap[r][c] = '.'
        for idx in range(4):
            nx = r + dx[idx]
            ny = c + dy[idx]
            if 0 <= nx < R and 0 <= ny < C:
                myMap[nx][ny] = '.'

    if time == N:
        break

for i in range(R):
    print(''.join(myMap[i]))

# ----------
# 풀이는 똑같은데 내가 작성한 코드는 왜 시간초과 인지 모르겠다..(85%까지 올라가다가 시간초과뜸)
# 16918, 봄버맨
import sys
from collections import deque


def loc_bombs():    # 폭탄 위치 찾아 bombs deque에 저장
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                bombs.append((i, j))


def make_bombs():   # 모든 자리에 폭탄 설치
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                board[i][j] = 'O'


def explode():      # bombs deque에 들어있는 좌표로 폭탄 터트림
    while bombs:
        r, c = bombs.popleft()
        board[r][c] = '.'
        if 0 <= r - 1:
            board[r - 1][c] = '.'
        if r + 1 < R:
            board[r + 1][c] = '.'
        if 0 <= c - 1:
            board[r][c - 1] = '.'
        if c + 1 < C:
            board[r][c + 1] = '.'


R, C, N = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

N -= 1  # 1초 동안 아무것도 하지 않는다
while N:
    bombs = deque()
    loc_bombs()
    make_bombs()
    N -= 1
    if N == 0:
        break
    explode()
    N -= 1

for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j], end='')
    print()