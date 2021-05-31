def check(row, col):

    if column_check[col] == 1:
        return False
    if diagonal_check[row + col] == 1:
        return False
    if diagonal_check2[row - col + N-1] == 1:
        return False

    return True

def DFS(row):
    if row == N:
        return 1
    answer = 0
    for col in range(N):
        if check(row, col):
            board[row][col] = 1
            column_check[col] = 1
            diagonal_check[row+col] = 1
            diagonal_check2[row-col+N-1] = 1
            answer += DFS(row+1)
            board[row][col] = 0
            column_check[col] = 0
            diagonal_check[row + col] = 0
            diagonal_check2[row - col + N - 1] = 0

    return answer

N = int(input())
board = [[0] * N for _ in range(N)]
column_check = [0] * N # 같은 열인지 체크하는 배열
diagonal_check = [0] * (2*N-1) # 같은 대각선인지 체크하는 배열
diagonal_check2 = [0] * (2*N-1) # 반대편 대각선 체크
print(DFS(0))