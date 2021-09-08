from collections import deque


def solution(priorities, location):
    answer = []
    queue = deque([(idx, value) for idx, value in enumerate(priorities)])

    while queue:
        work = queue[0]
        if work[1] == max(queue, key=lambda x: x[1])[1]:
            answer.append(work[0])
            queue.popleft()
        else:
            queue.append(queue.popleft())

    return answer.index(location) + 1

