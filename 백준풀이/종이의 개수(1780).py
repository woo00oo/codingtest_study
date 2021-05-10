def check(x, y, n):
    global paper
    pick = table[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if pick != table[i][j]:
                new_n = n // 3
                for ii in range(0, 3):
                    for jj in range(0, 3):
                        check(x + ii*new_n, y + jj*new_n, new_n)
                return

    paper[pick] += 1


N = int(input())
table = [list(map(int,input().split())) for _ in range(N)]
paper = [0, 0, 0] # 0의 개수, 1의 개수, -1의 개수
check(0, 0, N)
for i in range(-1, 2):
    print(paper[i])