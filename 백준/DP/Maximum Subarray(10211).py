T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0] * N
    li = list(map(int,input().split()))
    dp[0] = li[0]
    for i in range(1,N):
        dp[i] = max(li[i],dp[i-1]+li[i])
    print(max(dp))