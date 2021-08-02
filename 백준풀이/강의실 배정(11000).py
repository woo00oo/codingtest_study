# 시간 복잡도 O(nlogn)

import heapq
import sys

N = int(input())

timeTable = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
timeTable.sort(key=lambda x: x[0])

queue = []
heapq.heappush(queue, timeTable[0][1])

for i in range(1, N):
    if queue[0] > timeTable[i][0]:
        heapq.heappush(queue, timeTable[i][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, timeTable[i][1])

print(len(queue))


'''

강의 시간을 정렬 후 강의의 끝나는 시간을 다른 강의의 시작 시작관 비교

1) 시작 시간이 크거나 같다면 같은 강의실에서 강의를 할 수 있는 조건을 만족 -> 원래 있던 강의를 큐에서 삭제하고 시작 시간이 조건에 맞는 강의를 큐에 넣어줌

2) 시작 시간이 작으면 같은 강의실에서 강의를 할 수 없음 -> 기존 강의를 삭제하지 않고 시작 강의를 새롭게 큐에 삽입하여 다른 강의실을 필요로 한다는 것을 의미.



'''