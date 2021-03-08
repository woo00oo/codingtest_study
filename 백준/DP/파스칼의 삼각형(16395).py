# 문제풀이:
#   알고리즘은 금방 구현하였지만 인덱스 에러를 빨리 해결하지 못하였다.
#   인덱스 범위를 잘 생각하여 코드를 작성하는 능력을 키워야한다.

n, k = map(int,input().split())
dp = list()
for i in range(1,n+1):
    dp.append([0] * i)

for i in range(n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = 1
        elif i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
print(dp[n-1][k-1])