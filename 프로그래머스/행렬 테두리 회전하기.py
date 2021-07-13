def solution(rows, columns, queries):
    answer = []
    board = [[0] * columns for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = num
            num += 1

    for x1, y1, x2, y2 in queries:
        tmp = board[x1 - 1][y1 - 1]
        mini = tmp

        #왼쪽 세로
        for i in range(x1 - 1, x2 - 1):
            test = board[i + 1][y1 - 1]
            board[i][y1 - 1] = test
            mini = min(mini, test)

        #하단 가로
        for i in range(y1 - 1, y2 - 1):
            test = board[x2 - 1][i + 1]
            board[x2 - 1][i] = test
            mini = min(mini, test)

        #오른쪽 세로
        for i in range(x2 - 1, x1 - 1, -1):
            test = board[i - 1][y2 - 1]
            board[i][y2 - 1] = test
            mini = min(mini, test)

        #상단 가로
        for i in range(y2 - 1, y1 - 1, -1):
            test = board[x1 - 1][i - 1]
            board[x1 - 1][i] = test
            mini = min(mini, test)

        #값이 바뀌기 전의 값 = tmp을 넣어준다
        board[x1 - 1][y1] = tmp
        answer.append(mini)

    return answer