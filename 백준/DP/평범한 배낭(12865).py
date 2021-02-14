# 물건을 쪼갤 수 있다면 그리디로 쪼갤 수 없는 문제는 dp를 활용하여 해결.

N, K = map(int,input().split())
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    weight, value = map(int,input().split())
    for j in range(1, K+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[N][K])
