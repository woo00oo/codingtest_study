# 맨 마지막일 부터 거꾸로 계산.
n = int(input())
t = []
p = []
dp = [0] * (n+1)
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]]) # max(현재 일을 하지 않고 넘어갈 때의 이윤(i+1) , 현재 일의 이윤 + 현재 일이 필요한 day뒤의 이윤)
print(dp[0])