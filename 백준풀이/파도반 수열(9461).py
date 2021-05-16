# 5번째 삼각형까진 특정 패턴이 없고 6번째 삼각형부터 패턴을 찾을 수 있다.

T = int(input())

for _ in range(T):
    N = int(input())
    dp = [1, 1, 1, 2, 2]

    if N <= 5:
        print(dp[N-1])
        continue

    for i in range(5, N):
        dp.append(dp[i-1] + dp[i-5])

    print(dp[N-1])
