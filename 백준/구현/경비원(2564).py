b_w, b_h = map(int, input().split())
# 좌표의 점을 배열의 칸으로 표현하기 위해서
# 가로, 세로 길이에 1씩 더해주었다.
brd = [[0 for _ in range(b_w+1)] for __ in range(b_h+1)]
# 상점 개수 -> N
N = int(input())
# 주어지는 위치를 활용하여 brd에 상점을 표시
for i in range(1, N+1):
    store = list(map(int, input().split()))
    # 상점이 북쪽에 있는 경우
    if store[0] == 1:
        brd[0][store[1]] = i
    # 상점이 남쪽에 있는 경우
    if store[0] == 2:
        brd[b_h][store[1]] = i
    # 상점이 서쪽에 있는 경우
    if store[0] == 3:
        brd[store[1]][0] = i
    # 상점이 동쪽에 있는 경우
    if store[0] == 4:
        brd[store[1]][b_w] = i

# 경비원이 동서남북 중에서 어디에 있느냐에 따라
# 델타값이 달라져야한다.
# 경비원의 위치도 brd에서 활용할 수 있도록 변경한다.
tmp_r, tmp_c = map(int, input().split())
if tmp_r == 1:
    cwr_idx = 0
    ccwr_idx = 2
    g_r, g_c = 0, tmp_c
if tmp_r == 2:
    cwr_idx = 2
    ccwr_idx = 0
    g_r, g_c = b_h, tmp_c
if tmp_r == 3:
    cwr_idx = 3
    ccwr_idx = 3
    g_r, g_c = tmp_c, 0
if tmp_r == 4:
    cwr_idx = 1
    ccwr_idx = 1
    g_r, g_c = tmp_c, b_w

# 시계 방향으로 돌면서 가게와의 거리 체크
# 각 원소에는 가게와의 거리를 담을 것이다.
cwr = [0] * (N+1)
# 우 -> 하 -> 좌 -> 상
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 경비원이 원래 자리로 돌아오기 위해서 걸어야하는 거리는
# 사각형 블록 변의 총합이랑 같다.
n_g_r, n_g_c = g_r, g_c
for i in range(1, (b_w+b_h)*2 + 1):
    # 경비원의 다음 위치가 주어진 조건을 벗어나는 경우 -> 벽을 넘어가려고 하는 경우
    # 방향 전환을 한다.
    if n_g_r + drc[cwr_idx][0] < 0 or n_g_r + drc[cwr_idx][0] > b_h \
            or n_g_c + drc[cwr_idx][1] < 0 or n_g_c + drc[cwr_idx][1] > b_w:
        cwr_idx = (cwr_idx+1) % 4
        n_g_r += drc[cwr_idx][0]
        n_g_c += drc[cwr_idx][1]
    else:
        n_g_r += drc[cwr_idx][0]
        n_g_c += drc[cwr_idx][1]
    # 만약 방문한 곳이 가게라면 그 가게를 가기위해서
    # 걸었던 거리를 저장
    if brd[n_g_r][n_g_c]:
        cwr[brd[n_g_r][n_g_c]] = i

# 반시계 방향으로 돌면서 가게와의 거리 체크
ccwr = [0] * (N+1)
# 우 -> 상 -> 좌 -> 하
drc = [(0, 1), (-1, 0), (0, -1), (1, 0)]
# 경비원이 원래 자리로 돌아오기 위해서 걸어야하는 거리는
# 사각형 블록 변의 총합이랑 같다.
n_g_r, n_g_c = g_r, g_c
for i in range(1, (b_w+b_h)*2 + 1):
    # 경비원의 다음 위치가 주어진 조건을 벗어나는 경우 -> 벽을 넘어가려고 하는 경우
    # 방향 전환을 한다.
    if n_g_r + drc[ccwr_idx][0] < 0 or n_g_r + drc[ccwr_idx][0] > b_h \
            or n_g_c + drc[ccwr_idx][1] < 0 or n_g_c + drc[ccwr_idx][1] > b_w:
        ccwr_idx = (ccwr_idx+1) % 4
        n_g_r += drc[ccwr_idx][0]
        n_g_c += drc[ccwr_idx][1]
    else:
        n_g_r += drc[ccwr_idx][0]
        n_g_c += drc[ccwr_idx][1]
    # 만약 방문한 곳이 가게라면 그 가게를 가기위해서
    # 걸었던 거리를 저장
    if brd[n_g_r][n_g_c]:
        ccwr[brd[n_g_r][n_g_c]] = i
# 시계 방향과 반시계 방향중 더 짧은 거리를
# 반환할 값에 더해준다.
total = 0
for i in range(1, N+1):
    if cwr[i] < ccwr[i]:
        total += cwr[i]
    else:
        total += ccwr[i]
print(total)