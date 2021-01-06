# 통과는 하였지만 다른 풀이에 비해 시간이 오래 걸려서 다른 사람들의 코드를 참고하였다.

# _____내풀이 ______
#import sys
#
# testcaseNum = int(input())
# for _ in range(testcaseNum):
#     N = int(input())
#     set_state = list(sys.stdin.readline().strip())
#     goal_state = list(sys.stdin.readline().strip())
#     BW_list = list()
#     WB_list = list()
#     count = 0
#
#     for index in range(N):
#         if set_state[index] != goal_state[index]:
#             if set_state[index] == 'B':
#                 BW_list.append(index)
#             else:
#                 WB_list.append(index)
#
#     for index in range(len(BW_list)):
#
#         if len(WB_list) != 0 :
#             change_index = WB_list.pop(0)
#             set_state[BW_list[index]], set_state[change_index] = set_state[change_index], set_state[BW_list[index]]
#             count += 1
#
#         else:
#             set_state[BW_list[index]] = 'W'
#             count +=1
#
#     for index in range(len(WB_list)):
#         set_state[WB_list[index]] = 'B'
#         count += 1
#
#     print(count)


#_______다른 사람 풀이 ______
# set_state와 goal_state의 같은 인덱스 기준 값이 다를 때 'B'인 경우와 'W'의 경우의 합 중 최대값(max)가 정답이다. ( 정답을 구할 수 있는 연관성을 생각해보기 !!)
import sys


testCaseNum = int(input())
for _ in range(testCaseNum):
    N = int(input())
    set_state = list(sys.stdin.readline().strip())
    goal_state = list(sys.stdin.readline().strip())
    B,W = 0, 0
    for i in range(N):
        if set_state[i] == goal_state[i] :
            continue
        if set_state[i] == 'B':
            B += 1
        else:
            W += 1
    print(max(B,W))




