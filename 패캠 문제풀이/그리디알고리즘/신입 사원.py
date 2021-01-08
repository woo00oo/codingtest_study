#실패 코드 : 2중 for문으로 인한 시간초과

# import sys
#
# test_case_num = int(input())
#
# for _ in range(test_case_num):
#     N = int(input())
#     rank_list = list()
#     count = 1
#     for _ in range(N):
#         test1, test2 = list(map(int,sys.stdin.readline().split()))
#         rank_list.append((test1,test2))
#     rank_list.sort(key=lambda x:x[0])
#
#     for index in range(1,N):
#         hire = True
#         for i in range(index-1,-1,-1):
#             if rank_list[index][1] > rank_list[i][1]:
#                 hire = False
#                 break
#         if hire:
#             count += 1
#
#     print(count)

# 문제 해결 :
#   시간초과의 문제를 해결하기 위해 변수 min을 사용하여, 여태 지나왔던 지원자들의 면접 시험 성적중 가장 좋은 면접시험 성적을 저장함.
#   그렇게되면 특정 지원자의 i의 면접 시험 성적과 min만 비교하여 특정 지원자 i가 선발될지 파악할 수 있음.

import sys

test_case_num = int(input())

for _ in range(test_case_num):
    N = int(input())
    rank_list = list()

    for _ in range(N):
        test1, test2 = list(map(int,sys.stdin.readline().split()))
        rank_list.append((test1,test2))
    rank_list.sort(key=lambda x:x[0])

    count = 1
    min = rank_list[0][1]

    for index in range(1,N):
        if rank_list[index][1] < min:
            min = rank_list[index][1]
            count +=1
    print(count)