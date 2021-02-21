# 점화식 : dp(N) = min(dp[n//3]+1, dp[n//2]+1, dp[n-1]+1)

X = int(input())
dp = [0] * 1000001
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4,X+1):
    num1,num2 = 1000001, 1000001
    if i % 2 == 0:
        num1 = 1 + dp[i//2]
    if i % 3 == 0:
        num2 = 1 + dp[i//3]
    num3 = 1 + dp[i-1]
    dp[i] = min(num1,num2,num3)

print(dp[X])


