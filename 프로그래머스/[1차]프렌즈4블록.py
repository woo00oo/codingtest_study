dx = [0, +1, +1]
dy = [+1, 0, +1]


def four_block_check(m, n, i, j, board, removed):

    check = 1
    for idx in range(3):
        nx = i + dx[idx]
        ny = j + dy[idx]

        if 0 <= nx < m and 0 <= ny < n:
            if board[nx][ny] == board[i][j]:
                check += 1

    # 4개 블록이 붙어 있다면
    if check == 4:
        if (i, j) not in removed:
            removed.add((i, j))
        for idx in range(3):
            nx = i + dx[idx]
            ny = j + dy[idx]
            if (nx, ny) not in removed:
                removed.add((nx, ny))

    return removed


def block_down(m, n, board):
    for j in range(n):
        for i in range(m - 2, -1, -1):
            if board[i][j] != '.':
                for x in range(i + 1, m):
                    if board[x][j] == '.':
                        board[x][j] = board[x - 1][j]
                        board[x - 1][j] = '.'
                    else:
                        break


def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list((board[i]))

    while True:
        # 4개 블록 체크
        removed = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] != '.':
                    four_block_check(m, n, i, j, board, removed)

        # 지워질 블럭이 없으면 종료.
        if len(removed) == 0:
            break

        # '.'으로 변환
        for i, j in removed:
            answer += 1
            board[i][j] = '.'

        # 블럭 밑으로 내리기
        block_down(m, n, board)

    return answer

