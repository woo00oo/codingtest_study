# n의 최대값이 35이므로 dp 리스트의 길이를 36까지 생성

n = int(input())
dp = [0] * 36
dp[0] = 1

for number in range(1, n+1):
    n1, n2 = 0, number-1
    while True:
        if n1 == n:
            break
        dp[number] += dp[n1] * dp[n2]
        n1 += 1
        n2 -= 1

print(dp[n])