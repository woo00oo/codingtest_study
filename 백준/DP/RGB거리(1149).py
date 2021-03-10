# 문제풀이:
#   0,1,2는 각각 빨강, 초록, 파랑
#   dp[i][0] = i번째 집을 빨강으로 칠했을때의 최소값을 나타냄
#   빨강, 초록, 파랑을 모두 구해 최소값을 출력시키면 해결.


N = int(input())
dp = list()
for i in range(N):
    dp.append(list(map(int,input().split())))

for i in range(1,N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]

print(min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))
