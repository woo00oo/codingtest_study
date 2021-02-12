# round 함수 => 반올림 해주는 함수, 2번째 인자에 소수 몇번째 자리 나타낼 것인지 나타냄
# 브루트 포스로 해결하려고 하였지만 시간초과, DP 활용
# import sys
#
# N = int(input())
# numbers = [float(sys.stdin.readline().strip()) for _ in range(N)]
# answer = 0
#
# for i in range(1, N+1):
#     for j in range(N+1-i):
#         ex = numbers[j:j+i+1]
#         Max = 1
#         for num in ex:
#             Max *= num
#         if Max > answer:
#             answer = Max
#
# print(round(answer, 3))


N = int(input())
numbers = [float(input()) for _ in range(N)]
dp = [0] * N
dp[0] = numbers[0]
for i in range(1, N):
    dp[i] = max(dp[i-1] * numbers[i], numbers[i])

print("%.3f" % max(dp))



