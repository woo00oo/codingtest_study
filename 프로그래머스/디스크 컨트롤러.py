# 첫번째 시도 :
#   단순 작업이 요청되는 시간 + 작업의 소요시간 순으로 정렬해서 평균 값을 구해줌
#   현재 시점에서 처리할 수 있는 작업들을 고려하지 않음 ex) 현재 시점은 3이지만 요청한 시점은 5라면 컨트롤러는 작동하지 않음
#

def solution1(jobs):
    jobs = sorted(jobs, key=lambda x: (x[0] + x[1],x[0]))
    times = []
    Sum = 0

    for i in range(len(jobs)):
        Sum += jobs[i][1]
        times.append(Sum-jobs[i][0])

    answer = sum(times) // len(times)

    return answer

# 2번째 시도:
#   현재 시점에서 처리할 수 있는 작업들 중에서 작업의 소요 시간 먼저 처리 해주는 방식으로 해결.
#   현재 시점에서 처리할 수 있는 작업들을 힙에 넣고, 하나를 뽑아 현재 시점과 총 대기시간을 구해주는 것을 모든 작업을 처리할 때 까지 반복
#   현재 시점에서 처리할 수 있는 작업인지를 판별하는 조건은 작업의 요청 시간이 바로 이전에 완료한 작업의 시작시간보다 크고, 현재 시점보다 작거나 같아야 한다.
#   만약 현재 처리할 수 있는 작업이 없다면, 남아 있는 작업들의 요청 시간이 아직 오지 않은 것이기 때문에 현재 시점을 하나 올려준다.

import heapq

def solution2(jobs):
    answer, now, work, = 0, 0, 0
    start = -1
    heap = []

    # jobs의 길이 만큼 작업을 처리 했을 때 까지 반복
    while work < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1],job[0]]) # 첫번째 원소를 기준으로 최소 힙을 구성.

        if len(heap) > 0:
            current_job = heapq.heappop(heap)
            start = now
            now += current_job[0]
            answer += (now - current_job[1])
            work += 1 # 하나의 작업을 처리함
        else:
            now += 1

    return answer // len(jobs)


