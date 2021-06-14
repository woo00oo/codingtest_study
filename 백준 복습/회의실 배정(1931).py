# 회의가 빨리 끝나는 시간 순으로 오름차순 정리
# 회의가 끝나는 시간이 같다면 먼저 회의를 시작한 순으로 오름차순 정리


import sys

N = int(input())

meeting = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    meeting.append((start, end))

meeting.sort(key=lambda x: (x[1], x[0]))

count = 1
end_time = meeting[0][1]
for i in range(1, N):
    if meeting[i][0] >= end_time:
        count += 1
        end_time = meeting[i][1]

print(count)
