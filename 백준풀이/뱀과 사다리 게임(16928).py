# check_move가 사다리거나 뱀일 경우 값을 해당 이동값으로 수정해준다.

from collections import deque

def BFS():
    queue = deque([1])
    visited[1] = True

    while queue:
        now = queue.popleft()
        for move in range(1, 7):
            check_move = now + move
            if 0 < check_move <= 100 and not visited[check_move]:
                if check_move in ladder.keys():
                    check_move = ladder[check_move]

                if check_move in snake.keys():
                    check_move = snake[check_move]

                if not visited[check_move]:
                    queue.append(check_move)
                    visited[check_move] = True
                    board_cnt[check_move] = board_cnt[now] + 1

N, M = map(int, input().split())
board_cnt = [0] * 101
visited = [False] * 101

snake = dict()
ladder = dict()

for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

BFS()
print(board_cnt[100])




