# deque.rotate를 활용하여 쉽게 풀이
# rotate(v)
# v > 0 : 오른쪽으로 v만큼 회전
# v < 0 : 왼쪽으로 v만큼 회전

from collections import deque

def solution(A, K):
    queue = deque(A)
    queue.rotate(K)

    return list(queue)


print(solution([3, 8, 9, 7, 6], 3))