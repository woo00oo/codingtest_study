N = int(input())
numbers = [float(input()) for _ in range(N)]
dp = [0] * N
dp[0] = numbers[0]

for i in range(1, N):
    dp[i] = max(numbers[i], dp[i-1] * numbers[i])

print("%.3f" % max(dp))

