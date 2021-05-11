def check(x, y, n):
    global answer
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                new_n = n // 2
                for new_i in range(2):
                    for new_j in range(2):
                        check(x+new_i*new_n, y+new_j*new_n, new_n)

                return
    answer[color] += 1


N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
answer = [0, 0]
check(0,0,N)
print(answer[0])
print(answer[1])