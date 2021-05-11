# 2차원 배열 dp
#   이전 계단을 밟았을 경우, 밟지 않았을 경우의 최대값을 더해 나간다
#                       10     20      15
# 이전 계단 밟은 경우        10     30      35(15+20) => 이전 계단을 밟았을 경우에는 그 이전 계단에서 그 전 계단을 밟지 않았을 경우를 더해준다 ( 3번 연속 밟을수 없음)
# 이전 계단 밟지 않은 경우    10     20      15 + max(10,10) => 이전 계단을 밟지 않았을 경우에는 2칸 전 계단에서 이전 계단을 밟은 경우와 이전 계단을 밟지 않은 경우의 최대값이랑 더해줌.


N = int(input())
stairs = [int(input()) for _ in range(N)]
dp = [[0]*N for _ in range(2)]
if N == 1:
    print(stairs[0])
    exit(0)
if N == 2:
    print(sum(stairs))
    exit(0)
dp[0][0] = stairs[0]
dp[1][0] = stairs[0]
dp[0][1] = stairs[0] + stairs[1]
dp[1][1] = stairs[1]

for i in range(2,N):
    dp[0][i] = stairs[i] + dp[1][i-1]
    dp[1][i] = stairs[i] + max(dp[0][i-2], dp[1][i-2])

print(max(dp[0][-1], dp[1][-1]))