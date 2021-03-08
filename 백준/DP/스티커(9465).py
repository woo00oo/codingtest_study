# 문제풀이:
#   1번째 인덱스 = 왼쪽 대각선의 숫자를 더 할 수 있음
#   2번째 인덱스부터는 max(이때까지 최댓값을 더한 숫자를 저장하고 있는 왼쪽 대각선의 숫자 , 그 왼쪽 숫자) + 현재 숫자

# dp의 점화식을 잘 생각해 보자

t = int(input())
for i in range(t):
    dp = list()
    n = int(input())

    for _ in range(2):
        dp.append(list(map(int, input().split())))

    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for j in range(2, n):
        dp[0][j] += max(dp[1][j - 1], dp[1][j - 2])
        dp[1][j] += max(dp[0][j - 1], dp[0][j - 2])

    print(max(dp[0][n - 1], dp[1][n - 1]))