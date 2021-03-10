R, C, W = map(int,input().split())
R -= 1
C -= 1
dp = [[0] * i for i in range(1,R+W+1)]
answer = 0
for i in range(R+W):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = 1
        elif i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

for i in range(W):
    for j in range(i+1):
        answer += dp[R+i][C+j]
print(answer)
