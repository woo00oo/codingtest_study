# deque.rotate() -> 큐를 회전해주는데 용이한 메서드 ( 음수값일 경우 왼쪽으로 그 수 만큼 회전, 양수값일 경우 오른쪽으로 그 수 만큼 회전)

from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    queue = deque(map(int, input().split()))
    queue = deque((index,value) for index, value in enumerate(queue))
    answer = 0
    while True:
        if queue[0][1] == max(queue, key=lambda x:x[1])[1]:
            answer += 1

            if queue[0][0] == M:
                print(answer)
                break
            else:
                queue.popleft()
        else:
            queue.rotate(-1)

