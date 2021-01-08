# 리스트를 시작하는 시간의 오름 차순으로 정렬한 뒤 문제를 풀려고 하니 로직이 복잡해 지는 문제가 발생하였다.
# 회의가 짧게 걸리는 순으로 선택해주면 정답이 되는것을 알 고 있었지만 정렬을 잘못해주어 로직을 짜누는데 어려움을 겪었다.

# N = int(input())
# meeting_list = list()
#
# for _ in range(N):
#     start, end = list(map(int,input().split()))
#     meeting_list.append((start,end))
# meeting_list.sort(key=lambda x:x[0])
# time = 0
# count = 0
# add_meeting = meeting_list[0]
# i = 0
# while True:
#     if time > meeting_list[-1][0]:
#         break
#     for index in range(i+1,N):
#         if add_meeting[1] - time < meeting_list[index][1] - time:
#             break
#         if add_meeting[1] - time > meeting_list[index][1] - time:
#             add_meeting = meeting_list[index]
#             i = index
#     time = add_meeting[1]
#     count +=1
#     add_meeting = meeting_list[i+1]
# print(count)
# -------------
#문제 해결 능력
#   끝나는 시간의 오름차순, 시작하는 시간의 오름차순으로 정렬.

import sys

N = int(input())
meeting_list = list()

for _ in range(N):
    start, end = list(map(int,sys.stdin.readline().split()))
    meeting_list.append((start,end))

# 정렬을 하는 방법은 2가지가 있다.
# case1 : 전체를 시작시간의 오름차순으로 정렬을 한 뒤, 정렬된 리스트를 다시 끝나는 시간으로 오름차순으로 정렬.
# meeting_list.sort(key=lambda x: x[0])
# meeting_list.sort(key=lambda x: x[1])

# case2 : 한번에 정렬
meeting_list.sort(key=lambda x:(x[1],x[0]))

count = 1
end_time = meeting_list[0][1]
for i in range(1,N):
    if meeting_list[i][0] >= end_time:
        count +=1
        end_time = meeting_list[i][1]
print(count)
