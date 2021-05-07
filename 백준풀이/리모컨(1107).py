# 첫번째 풀이 : 무식하게 풀기
# 채널을 위, 아래로 순회하면서 고장난 리모콘으로 채널 이동이 가능할때 까지 반복문을 돌린다 => 시간 초과

# N = input()
# M = int(input())
# buttons = list(input().split())
# count_miner = 0
# count_plus = 0
# channel_miner = N
# channel_plus = N
# if N == '100':
#     print(0)
#     exit(0)
# while True:
#     plus, minus = True, True
#     for i in range(len(channel_miner)):
#         if channel_miner[i] in buttons:
#             channel_miner = str(int(channel_miner) - 1)
#             minus = False
#             break
#
#     for i in range(len(channel_plus)):
#         if channel_plus[i] in buttons:
#             channel_plus = str(int(channel_plus) + 1)
#             plus = False
#             break
#
#     if minus:
#         count_miner += len(channel_miner)
#         count_miner += abs(int(N) - int(channel_miner))
#         print(count_miner)
#         break
#     if plus:
#         count_plus += len(channel_plus)
#         count_plus += abs(int(N) - int(channel_plus))
#         print(count_plus)
#         break


# ----------------------------------------------

# case1: 현재채널(100)에서 그냥 희망채널까지 +- 버튼으로 이동했을 때의 횟수
# case2: 모든 채널을 순회하면서 해당 채널에서 희망채널까지 +- 버튼으로 이동했을때의 횟수 ( 1 ~ 9 버튼으로 채널 이동후 +-)
# case1과 case2의 최소 값을 출력

N = int(input())
M = int(input())
# 0 ~ 9 까지 버튼을 가지고 있는 리모컨
remote_controller = {str(i) for i in range(10)}

# 고장난 버튼은 리모컨에서 제거
if M > 0:
    remote_controller -= set(map(str, input().split()))

current_channel = 100
# 현재 보고 있는 채널에서 보고자 하는 채널까지 +- 버튼을 통해 이동했을때 버튼을 눌러야하는 횟수
min_cnt = abs(current_channel-N)

# 100만 채널까지 순회
# 최대 희망 채널은 50만인데 100만까지 순회 하는 이유는 +인 경우가 최적일때와 - 인 경우가 최적일때를 모두 고려하려면 100만까지 순회를 해야 값을 구해야 한다.
# ex) 희망 채널이 40만 고장난 버튼이 1,2,3,4,5 일 경우 60만 채널에서 - 로 줄이는 경우가 최적이다.
for channel in range(1000000):
    for j in range(len(str(channel))):
        # 고장난 자릿수일 경우
        if str(channel)[j] not in remote_controller:
            break
        # 채널 이동이 가능한 경우 min_cnt 초기화
        elif len(str(channel)) - 1 == j:
            min_cnt = min(min_cnt, abs(channel-N) + len(str(channel)))

print(min_cnt)