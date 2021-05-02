# 1차 시도 => 메모리 초과

# N = int(input())
# dp = [[] for _ in range(N+1)]
# dp[1] = ['1']
# for i in range(2,N+1):
#     for j in range(len(dp[i-1])):
#         if dp[i-1][j][-1] == '1':
#             dp[i].append(dp[i-1][j] + '0')
#         else:
#             dp[i].append(dp[i-1][j] + '1')
#             dp[i].append(dp[i-1][j] + '0')
#
# print(len(dp[N]))

# 2차 시도 (규칙을 발견)
N = int(input())
dp = [0] * 91
dp[1] = 1
dp[2] = 1
if N <= 2:
    print(dp[N])
    exit(0)

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])