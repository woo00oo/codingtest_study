from collections import deque

N = int(input())
queue = deque([i for i in range(1, N+1)])

answer = []

while len(queue) != 1:
    answer.append(queue.popleft())
    queue.append(queue.popleft())

answer.append(queue[-1])

print(*answer)