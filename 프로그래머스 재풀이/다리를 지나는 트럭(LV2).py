'''
첫번째 풀이 : 시간초과
rotate() 때문에 하나의 테스트 케이스에서 시간초과가 발생한 듯 싶다.

'''

from collections import deque


def timePlus(queue):
    if queue[0] != 0:
        queue[0] = 0

    queue.rotate(-1)


def solution(bridge_length, weight, truck_weights):
    answer = 1
    queue = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    while truck_weights:

        # 트럭이 다리 위로 올라갈 수 있는지?
        if truck_weights[0] + sum(queue) <= weight:
            queue[-1] = truck_weights[0]
            truck_weights.popleft()

        # 1초 경과
        answer += 1
        timePlus(queue)

    while sum(queue) != 0:
        answer += 1
        timePlus(queue)

    return answer


# --------------
'''
rotate로 모든 원소를 왼쪽으로 미는 것이 아닌 
큐의 맨 앞, 맨 뒤 부분만 신경 써준다.

'''


def solution(bridge_length, weight, truck_weights):
    time = 0
    queue = [0] * bridge_length

    while queue:
        time += 1
        queue.pop(0)
        if truck_weights:
            if sum(queue) + truck_weights[0] <= weight:
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)

    return time
