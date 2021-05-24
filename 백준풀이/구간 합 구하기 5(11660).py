# 첫번째 시도 : 시간 초과
# 시간복잡도 O(n^2)
# 반복문으로 해당하는 값들을 일일히 순회하면서 더함
# 여러 구간 합을 구해야할 경우는 비효율적.

# N, M = map(int, input().split())
# table = [list(map(int, input().split())) for _ in range(N)]
# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     answer = 0
#     for i in range(x1-1, x2):
#         for j in range(y1-1, y2):
#             answer += table[i][j]
#     print(answer)

# 두번째 시도: 누적합을 활용하여 풀이.

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dp = [[0] * (n+1) for _ in range(n + 1)]
s = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(n):
        dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j]) + s[i][j]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])