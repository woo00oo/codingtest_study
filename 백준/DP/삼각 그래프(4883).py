# 점화식 = dp 1행 부분만 다르게 초기화.
# 문제에서 나타나는 화살표 방향으로 갈 수 있는 경우에서 젤 작은 값을 최신해 나간다.

k = 1
while True:
    N = int(input())
    if N == 0:
        exit(0)
    dp = []
    for _ in range(N):
        arr = list(map(int, input().split()))
        dp.append(arr)
    dp[1][0] = dp[0][1] + dp[1][0]
    dp[1][1] = dp[1][1] + min(dp[0][1], dp[0][1] + dp[0][2], dp[1][0])
    dp[1][2] = dp[1][2] + min(dp[0][1], dp[0][1] + dp[0][2], dp[1][1])

    for i in range(2,N):
        dp[i][0] = min(dp[i-1][0],dp[i-1][1]) + dp[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][1],dp[i-1][2],dp[i][0]) + dp[i][1]
        dp[i][2] = min(dp[i-1][1],dp[i-1][2],dp[i][1]) + dp[i][2]
    print(str(k)+'. '+str(dp[-1][1]))
    k += 1

