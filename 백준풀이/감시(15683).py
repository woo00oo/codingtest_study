from itertools import product

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
direction = [0, 1, 2, 3]
cctv_direction = {1: [[(0, +1)], [(+1, 0)], [(0, -1)], [(-1, 0)]],
             2: [[(0, +1), (0, -1)], [(+1, 0), (-1, 0)], [(0, +1), (0, -1)], [(+1, 0), (-1, 0)]],
             3: [[(0, +1), (-1, 0)], [(0, +1), (+1, 0)], [(0, -1), (+1, 0)], [(-1, 0), (0, -1)]],
             4: [[(-1, 0), (0, -1), (0, +1)], [(-1, 0), (+1, 0), (0, +1)], [(0, -1), (0, +1), (+1, 0)], [(-1, 0), (+1, 0),(0, -1)]],
             5: [[(+1, 0), (-1, 0), (0, +1), (0, -1)], [(+1, 0), (-1, 0), (0, +1), (0, -1)], [(+1, 0), (-1, 0), (0, +1),(0, -1)], [(+1, 0), (-1, 0), (0, +1), (0, -1)]]
             }
cctv_location = []
wall_count = 0

for i in range(N):
    for j in range(M):
        if office[i][j] == 1:
            cctv_location.append((i, j, 1))
        elif office[i][j] == 2:
            cctv_location.append((i, j, 2))
        elif office[i][j] == 3:
            cctv_location.append((i, j, 3))
        elif office[i][j] == 4:
            cctv_location.append((i, j, 4))
        elif office[i][j] == 5:
            cctv_location.append((i, j, 5))
        elif office[i][j] == 6:
            wall_count += 1

cctv_len = len(cctv_location)
if cctv_len == 1:
    cases = [[0], [1], [2], [3]]
else:
    cases = list(product(direction, repeat=cctv_len))

max_watch_area = 0
for i in range(len(cases)):
    watch_area = 0
    visited = [[0] * M for _ in range(N)]
    for j in range(len(cases[i])):
        x, y, cctv_type = cctv_location[j]
        d = cases[i][j]

        for search in range(len(cctv_direction[cctv_type][d])):
            dx, dy = x, y
            while True:
                nx = dx + cctv_direction[cctv_type][d][search][0]
                ny = dy + cctv_direction[cctv_type][d][search][1]

                if 0 <= nx < N and 0 <= ny < M and office[nx][ny] != 6:
                    if visited[nx][ny] == 0 and office[nx][ny] == 0:
                        watch_area += 1
                        visited[nx][ny] = 1

                    dx = nx
                    dy = ny
                else:
                    break

    if watch_area > max_watch_area:
        max_watch_area = watch_area

answer = M*N - wall_count - max_watch_area - cctv_len
print(answer)



