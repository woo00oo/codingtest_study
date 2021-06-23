myBoard = [list(map(int, input().split())) for _ in range(5)]
numbers = [list(map(int, input().split())) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]

answer = 1

for i in range(5):
    for j in range(5):

        num = numbers[i][j]

        # 빙고판 숫자 체크
        for x in range(5):
            for y in range(5):
                if myBoard[x][y] == num:
                    visited[x][y] = 1


        three_binggo = 0

        # 빙고 체크 가로
        for idx in range(5):
            if sum(visited[idx]) == 5:
                three_binggo += 1

        # 빙고 체크 세로
        for idx in range(5):
            binggo = True
            for idx2 in range(5):
                if visited[idx2][idx] == 0:
                    binggo = False
                    break
            if binggo:
                three_binggo += 1

        # 빙고 체크 (왼쪽위 -> 오른쪽아래)대각선
        binggo = True
        for idx in range(5):
            if visited[idx][idx] == 0:
                binggo = False
                break
        if binggo:
            three_binggo += 1

        # 빙고 체크 (오른쪽위 ->왼쪽아래)대각선
        binggo = True
        idx2 = 4
        for idx in range(5):
            if visited[idx][idx2] == 0:
                binggo = False
                break
            idx2 -= 1

        if binggo:
            three_binggo += 1

        if three_binggo >= 3:
                print(answer)
                exit(0)

        answer += 1
