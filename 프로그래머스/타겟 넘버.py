# 첫번째 시도 : dp를 사용하여 해결하려고 하였지만 처음 - 으로 시작할 경우를 따지기 어려워 실패

def solution(numbers, target):
    N = len(numbers)
    answer = 0
    dp = [[0 for _ in range(1001)] for _ in range(N)]

    dp[0][numbers[0]] = 1

    for i in range(N-1):
        for j in range(1001):
            if dp[i][j] != 0:
                if 1 <= j + numbers[i+1] <= 1000:
                    dp[i+1][j + numbers[i+1]] += dp[i][j]
                if 1 <= j - numbers[i+1] <= 1000:
                    dp[i+1][j - numbers[i+1]] += dp[i][j]

    for i in range(N):
        if dp[i][target] != 0:
            answer += dp[i][target]

    return answer

# 완전 탐색으로 간단히 해결
# product -> 중복 순열

from itertools import product

def solution2(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

solution2([1,1,1,1,1],3)