def check(x, y, n):
    global answer

    point = play[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if point != play[i][j]:
                new_n = n // 2
                answer += '('
                for new_i in range(2):
                    for new_j in range(2):
                        check(x+new_i*new_n, y+new_j*new_n, new_n)
                answer += ')'
                return
    answer += str(point)



N = int(input())
play = [list(map(int, input())) for _ in range(N)]
answer = ''
check(0, 0, N)
print(answer)