# 문제풀이:
#   울타리의 최소 개수를 구하는 문제가 아니므로 울타리에 대한 제한 조건이 존재하지 않는다.
#   그러므로 인접할 양과 늑대가 인접할 때를 제외하고 모두 울타리로 채우면 된다.
#   모든 좌표를 탐색
#   1) 늑대일경우 : 상하좌우를 탐색하여 인접한 곳에 양이 있으면 flag 변수를 1로 변경
#   2) 양인 경우 : 그냥 넘어감
#   3) 빈칸인 경우 : 모두 울타리로 채워줌
import sys

R, C = map(int, sys.stdin.readline().split())
myMap = [list(sys.stdin.readline().strip()) for _ in range(R)]
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
flag = 0
for i in range(R):
    for j in range(C):
        if myMap[i][j] == 'W':
            for a in range(4):
                ni, nj = i + dx[a], j + dy[a]
                if ni < 0 or nj < 0 or ni == R or nj == C:
                    continue
                elif myMap[ni][nj] == 'S':
                    flag = 1
        elif myMap[i][j] == 'S':
            continue
        else:
            myMap[i][j] = 'D'

if flag == 1:
    print('0')
else:
    print('1')
    for i in myMap:
        print(''.join(i))