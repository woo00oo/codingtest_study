N, M = map(int, input().split())
r, c, d = map(int, input().split())
myMap = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
direction = [(0, -1, 3), (-1, 0, 0), (0, +1, 1), (+1, 0, 2)]
back = [(+1, 0), (0, -1), (-1, 0), (0, +1)]
dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]
stop = False
answer = 0
now_r, now_c, now_d = r, c, d
while not stop:

    # 현재 위치 청소
    if myMap[now_r][now_c] == 0 and visited[now_r][now_c] == 0:
        visited[now_r][now_c] = 1
        answer += 1

    #a
    if 0 <= now_r + direction[now_d][0] < N and 0 <= now_c + direction[now_d][1] < M:
        next_r = now_r + direction[now_d][0]
        next_c = now_c + direction[now_d][1]
        if myMap[next_r][next_c] == 0 and visited[next_r][next_c] == 0:
            now_r = next_r
            now_c = next_c
            now_d = direction[now_d][2]
            continue

    # c, d
    cleaned = True
    for i in range(4):
        next_r = now_r + dx[i]
        next_c = now_c + dy[i]
        if 0 <= next_r < N and 0 <= next_c < M:
            if myMap[next_r][next_c] == 0 and visited[next_r][next_c] == 0:
                cleaned = False
    if cleaned:
        next_r = now_r + back[now_d][0]
        next_c = now_c + back[now_d][1]
        if 0 <= next_r < N and 0 <= next_c < M and myMap[next_r][next_c] == 0:
            now_r = next_r
            now_c = next_c
            continue
        else:
            stop = True
            continue
    # b
    now_d = direction[now_d][2]

print(answer)

