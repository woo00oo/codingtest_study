# 동일한 문자를 발견했을 때, 바로 전의 위치의 공통 부문 문자열의 길이에 1을 더해 준다.

s1 = input()
s2 = input()
answer = 0

dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(dp[i][j], answer)

print(answer)


# 2차원 배열 초기화하는 방법

# 1. arr = [[0 for _ in range(A)] for _ in range(B)]

# 2. arr = [[0] * A for _ in range(B)]

# 3. arr = [[0] * A ] * B

# 3번 방법은 사용하지 말 것!
# * 사용하면, 주소값을 복사하여 2차원 배열을 만드는 것이기 때문에 arr[0][x]을 수정하면
# 같은 주소를 공유하는 arr[0][x], arr[1][x], arr[2][x] 의 값이 한번에 변경 되는 문제가 발생.