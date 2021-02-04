# 시간 초과
# import sys
#
# N, M = map(int,input().split())
# meet_arr = list()
# for _ in range(N):
#     meet = list(map(int,sys.stdin.readline().split()))
#     meet_arr.append(meet)
# meet_arr.sort(key=lambda x: (x[1],-x[0]),reverse=True)
# answer = 99999999999999
#
# for i in range(N):
#     sum_weight = 0
#     price = 0
#     choice = meet_arr[i:]
#     for j in range(len(choice)):
#         sum_weight += choice[j][0]
#         price = choice[0][1]
#     if sum_weight >= M:
#         if price < answer:
#             answer = price
#
# if answer == 99999999999999:
#     print(-1)
# else:
#     print(answer)
#문제풀이:
#   가격을 먼저 오름차순으로 정렬후에 무게를 기준으로 오름차순으로 정렬
import sys

N, M = map(int, sys.stdin.readline().strip().split())

li = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

li.sort(key=lambda x: (x[1], -x[0]))
print(li)
meet = 0
money = 0
check = 0
for i in range(len(li)):
    meet += li[i][0]
    if meet < M:
        if i >= 1 and (li[i][1] == li[i - 1][1]):
            money += li[i][1]
        else:
            money = li[i][1]
    else:
        check = 1
        if i >= 1 and (li[i][1] == li[i - 1][1]): #가격은 동일하지만 무게는 다를 경우
            money += li[i][1]
            for j in range(i + 1, len(li)):
                if li[j][1] != li[i][1]:
                    if money > li[j][1]:
                        money = li[j][1]
                        break
        else:
            money = li[i][1]

        break

if check == 1:
    print(money)
else:
    print(-1)
