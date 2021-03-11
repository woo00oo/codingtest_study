#  동물원 문제와 비슷한 DP문제
#  N번째에 어떤 경우가 올 수 있는지를 생각하자
#  N번째 경우에 빨강(0), 초록(1), 파랑(2)이 왔을 경우를 모두 계산해준뒤 젤 작은 값이 이 문제에서 원하는 정답.

N = int(input())
dp = [list(map(int,input().split())) for _ in range(N)]

for i in range(1,N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]

print(min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))