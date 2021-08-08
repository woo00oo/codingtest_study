N = int(input())
height = N * 2 - 1
dp = []
for i in range(height):
    dp.append(list(map(int, input().split())))

print(dp)

for i in range(1, height//2+1):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] += dp[i - 1][j]
        elif j == len(dp[i]) - 1:
            dp[i][j] += dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i][j] + dp[i - 1][j - 1], dp[i][j] + dp[i - 1][j])

for i in range(height//2+1, height):
    for j in range(len(dp[i])):
        dp[i][j] = max(dp[i][j] + dp[i - 1][j + 1], dp[i][j] + dp[i - 1][j])

print(dp[-1][-1])


