# 이동방향을 리스트에 저장했을 때, 리스트의 맨 뒤부터 시작해서 (방향 + 1) % 4의 방향으로 진행하는 규칙.

import sys

input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
a = [[0]*101 for _ in range(101)]

# 드래곤 커브 그리기
for _ in range(n):
    x, y, d, g = map(int, input().split())
    a[x][y] = 1
    move = [d]
    # 이동방향을 move에 저장
    for _ in range(g):
        temp = []
        for i in range(len(move)):
            temp.append((move[-i-1] + 1) % 4)
        move.extend(temp)
    # move에 저장한 이동방향을 하나씩 불러와서 이동.

    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        a[nx][ny] = 1
        x, y = nx, ny


# 정사각형 개수 체크
ans = 0
for i in range(100):
    for j in range(100):
        if a[i][j]:
            if a[i+1][j] and a[i][j+1] and a[i+1][j+1]:
                ans += 1
print(ans)