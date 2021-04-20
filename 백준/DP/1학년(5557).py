N = int(input())
arr = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N)]

# dp 0번 인덱스의 arr[0] 값을 1 증가한다. => 첫번째 숫자는 반드시 포함되어야 하기 때문
dp[0][arr[0]] += 1

# 1부터 N-2 까지의 idx를 기준으로 다음 숫자를 더하거나 뺐을 경우 0이상 20이하 일 경우에만 이전 경우의 수(dp[i-1][j])를 더해 준다.
# N - 1번째 숫자는 나와야 하는 결과이므로 N - 2 까지의 인덱스만 확인하면 된다.
for i in range(1, N - 1):
    for j in range(21):
        if dp[i - 1][j]:
            if j + arr[i] <= 20:
                dp[i][j + arr[i]] += dp[i - 1][j]
            if j - arr[i] >= 0:
                dp[i][j - arr[i]] += dp[i - 1][j]

# N - 2 번째 까지의 원소를 사용하여 arr[N-1]가 나올 수 있는 모든 경우의 수
print(dp[N - 2][arr[N - 1]])