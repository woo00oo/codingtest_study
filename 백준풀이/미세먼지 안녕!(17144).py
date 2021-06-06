# 문제 해결:
#   미세먼지 확산은 동시에 일어나기 때문에 2개의 배열을 활용 ( 확산이 일어나는 값을 즉시 업데이트하면 오류가 나기 때문)
#   공기청정기는 상,하 따로 관리한다 => 상은 반시계방향, 하는 시계 방향으로 순환

# 미세먼지 확산
def spread():
    for x in range(R):
        for y in range(C):
            if myMap[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    # 범위 벗어남
                    if not (0 <= nx < R and 0 <= ny <C):
                        continue
                    # 5보다 작으면 미세먼지가 확산하지 않음
                    if myMap[x][y] < 5:
                        continue
                    # 공기 청정기로는 확산하지 않음
                    if (nx, ny) == (air_cleaner[0], 0):
                        continue
                    if (nx, ny) == (air_cleaner[1], 0):
                        continue
                    cnt += 1
                    myMap2[nx][ny] += myMap[x][y] // 5
                myMap2[x][y] = myMap2[x][y] + myMap[x][y] - myMap[x][y]//5 * cnt

def clean():
    # 위쪽 반시계방향
    for i in range(air_cleaner[0] - 2, -1, -1):
        myMap2[i + 1][0] = myMap2[i][0] # 위 -> 아래
    for i in range(1, C):
        myMap2[0][i - 1] = myMap2[0][i] # 왼쪽 -> 오른쪽
    for i in range(1, air_cleaner[0] + 1):
        myMap2[i - 1][-1] = myMap2[i][-1] # 아래 -> 위
    for i in range(C - 2, 0, -1):
        myMap2[air_cleaner[0]][i + 1] = myMap2[air_cleaner[0]][i] # 오른쪽 -> 왼쪽
    myMap2[air_cleaner[0]][1] = 0 # 공기 청정기로 들어가면 정화

    # 아래쪽 시계방향
    for i in range(air_cleaner[1] + 2, R):
        myMap2[i - 1][0] = myMap2[i][0] # 아래 -> 위
    for i in range(1, C):
        myMap2[-1][i - 1] = myMap2[-1][i] # 왼쪽 -> 오른쪽
    for i in range(R - 2, air_cleaner[1] - 1, -1):
        myMap2[i + 1][-1] = myMap2[i][-1] # 위 -> 아래
    for i in range(C - 2, 0, -1):
        myMap2[air_cleaner[1]][i + 1] = myMap2[air_cleaner[1]][i] # 오른쪽 -> 왼쪽
    myMap2[air_cleaner[1]][1] = 0

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]
R, C, T = map(int, input().split())
myMap = [list(map(int, input().split())) for _ in range(R)]

# 공기 청정기 행 위치
air_cleaner = []
for i in range(R):
    if myMap[i][0] == -1:
        air_cleaner.append(i)

# 확산은 동시에 일어나기 때문에 빈 배열을 하나 더 만들어 준다.
myMap2 = [[0] * C for _ in range(R)]

# 1번 시행
spread()
clean()

# T - 1번 시행
for time in range(T-1):
    myMap = myMap2.copy()
    myMap2 = [[0] * C for _ in range(R)]
    spread()
    clean()

answer = 0
for i in range(R):
    for j in range(C):
        if myMap2[i][j] > 0:
            answer += myMap2[i][j]
print(answer)