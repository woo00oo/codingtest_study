H, W = map(int, input().split())
My_map = list()
answer = [[-1] * W for _ in range(H)]
for _ in range(H):
    My_map.append(list(input()))

for i in range(H):
    cloud = False
    for j in range(W):
        if My_map[i][j] == 'c':
            cloud = True
            answer[i][j] = 0
        elif cloud:
            answer[i][j] = answer[i][j - 1] + 1

for li in answer:
    print(*li)
