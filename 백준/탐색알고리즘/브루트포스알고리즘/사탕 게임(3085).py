import sys
N = int(sys.stdin.readline())
board = [list(map(str, input())) for _ in range(N)]
res = 0

def check(board):
    cnt = 0
    for i in range(N):
        cnt_row = 1
        cnt_col = 1
        for j in range(N - 1):
            if board[i][j] == board[i][j + 1]:
                cnt_row += 1
            else:
                cnt = max(cnt, cnt_row)
                cnt_row = 1

            if board[j][i] == board[j + 1][i]:
                cnt_col += 1
            else:
                cnt = max(cnt, cnt_col)
                cnt_col = 1
        cnt = max(cnt, cnt_row, cnt_col)
    return cnt

for i in range(N):
    for j in range(N - 1):
        #행 탐색
        if board[i][j] != board[i][j + 1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            res = max(res, check(board))
            board[i][j+1], board[i][j] = board[i][j], board[i][j+1]
        # 열 탐색
        if board[j][i] != board[j + 1][i]:
            board[j][i], board[j+1][i] = board[j+1][i],board[j][i]
            res = max(res, check(board))
            board[j+1][i], board[j][i] = board[j][i], board[j+1][i]

print(res)