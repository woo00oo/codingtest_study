# 문제에서 고려할 중요한 조건

# 1) 가장 처음 파이프는 (1, 1)와 (1, 2)를 차지하고 있고, 방향은 가로이다.
# 2) 파이프가 놓여진 방향에 따라 회전 방향이 결정된다.
# 3) 회전 방향에 따라 특정 칸이 무조건 비어있어야 한다.

# directions에 각 방향 별로 회전할 수 있는 방향을 저장해둔다.(가로 : 0, 세로 : 1, 대각선 : 2)
# cos에는 방향에 따른 좌표를 저장해둔다.
# 좌표는 파이프의 끝라인으로 처리 처음에 (1, 1) (1, 2) 에 놓여져 있으면 좌표는 (1,2)로 처리
# dp 테이블은 3차원으로 구성 -> 3 가지의 놓인 방향에 따른 경우의 수를 저장하기 위함.
# 해당 좌표에 가로로 놓여질 수 있고, 세로로 놓여질수 있고, 대각선으로 놓여질 수 있음

import sys


# check 함수 -> 이동 가능한지 체크 회전 방향이 대각선인지 or 가로/세로 방향인지에 따라 다르게 처리
# 만약 회전 방향이 가로/세로 방향이라면 한 칸만 비어 있으면 된다(myMap[ny][nx] == 0)
# 하지만 회전 방향이 대각선이라면 두 칸이 더 비어있어야 한다(myMap[ny-1][nx] == 0 and myMap[ny][nx-1] == 0)

def check(y, x, d):
    for direction in directions[d]:
        dy, dx = cos[direction]
        ny = y + dy
        nx = x + dx

        if 0 <= ny < N and 0 <= nx < N and not myMap[ny][nx]:
            # 대각선이 아니면
            if direction != 2:
                dp[ny][nx][direction] += dp[y][x][d]
            else: # 대각선이면
                if not myMap[ny-1][nx] and not myMap[ny][nx-1]:
                    dp[ny][nx][direction] += dp[y][x][d]

directions = {0: [0, 2], 1: [1, 2], 2: [0, 1, 2]}
cos = {0: [0, 1], 1: [1, 0], 2: [1, 1]} # (y, x)

N = int(input())
dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]
myMap = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp[0][1][0] = 1

# 3중 for문을 돌며 dp테이블에 접근하고 만약 dp[y][x][d] != 0이라면 check함수를 실행한다(d는 방향)
# 만약 dp[y][x][d] == 0 이라면 해당 칸으로 이동시킬 방법이 없다는 것을 의미한다.

for y in range(N):
    for x in range(N):
        for d in range(3):
            # dp[y][x][d] != 0 이고 벽이 아닐 경우(빈 공간일 경우)
            if dp[y][x][d] and not myMap[y][x]:
                check(y, x, d)

print(sum(dp[N-1][N-1]))