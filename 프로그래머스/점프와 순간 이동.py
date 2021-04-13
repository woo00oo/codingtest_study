# 문제풀이
#   n이 1이 될때 까지 2로 계속 나누어 준다
#   1) 2로 나누어 떨어지면 순간 이동을 하면 되기 때문에 answer가 증가 하지 않는다
#   2) 2로 나누어 떨어지지 않으면 즉 홀수 이기 때문에 answer에 1를 증가 시킨다


def solution(n):
    answer = 0
    while n != 1:
        if n % 2 != 0:
            answer += 1
        n //= 2

    return answer + 1

print(solution(6))