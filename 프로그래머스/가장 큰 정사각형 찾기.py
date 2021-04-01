# 브루트포스 알고리즘으로 풀 경우 시간 복잡도가 n^3이 나와 시간 초과 발생
# dp를 활용하여 풀이
# [1][1] 부터 네칸씩 memozation을 실행
# 아래 오른쪽 칸이 1이면 나머지 세칸 중 최소값에 1을 더한 값으로 갱신.
# itertools.chain 메소드 학습 => 각 리스트를 연결할때 사용

import itertools

def solution(board):

    width = len(board[0])
    height = len(board)

    for x in range(1,height):
        for y in range(1,width):
            if board[x][y] == 1:
                board[x][y] = min(board[x-1][y-1],board[x-1][y], board[x][y-1]) + 1

    return max(itertools.chain(*board))**2

solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])