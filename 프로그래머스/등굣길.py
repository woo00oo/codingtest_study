# 문제풀이 : dp를 활용한 풀이
# 왼쪽 위 집에서 부터 하나씩 모든 경우의 수를 계산하며 학교를 가면 되는 문제.
# 각 위치 = 왼쪽에서 오는 방법과 위에서 오는 방법을 더해줌
# 최단 경로로 가기 위해서는 (1,1)에서 오른쪽이나 아래로만 움직여야 한다.


def solution(m, n, puddles):
    answers = [[0] * (m+1) for i in range(n+1)]
    answers[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 처음 시작 위치
            if i == 1 and j == 1:
                continue
            # 물에 잠긴 지역은 아예 이동을 할 수 없으므로 0
            if [j, i] in puddles:
                answers[i][j] = 0
            # 그 외의 지역은 왼쪽에서 오는 방법 + 위에서 오는 방법
            else:
                answers[i][j] = answers[i-1][j] + answers[i][j-1]

    return answers[n][m] % 1000000007