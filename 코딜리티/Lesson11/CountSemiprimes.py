# 세미프라임은 두 프라임(소수)의 곱으로 표현되는 수를 세미 프라임이라고 한다.
# 소수 : 2, 3, 5, 7 있을때 -> 세미 프라임 : 2 * 2 , 2 * 3 , 2 * 5 등등

def solution(N, P, Q):

    # 세미 프라임을 구하기 위해 먼저 프라임을 구한다. (에라토스테네스의 체)
    # 최대값인 N의 절반만큼만 구해도 된다. 세미프라임은 두 프라임의 곱이기 때문
    numbers = [0] * (N + 1)
    prime_list = []
    for i in range(2, N // 2 + 1):
        if numbers[i] == 0:
            prime_list.append(i)
            for j in range(i*2, N+1, i):
                numbers[j] = 1

    # 세미 프라임을 구한다. 프라임 리스트를 가져와 각 값들의 곱을 세미프라임 리스트에 표시
    semi_prime_idx = [False] * (N + 1)
    prime_length = len(prime_list)
    for i in range(prime_length):
        for j in range(i, prime_length):
            data = prime_list[i] * prime_list[j]
            if data <= N:
                semi_prime_idx[data] = True
            else:
                break

    # 1부터 세미프라임이 몇 개가 있는지를 나타내는 리스트를 만들고 각 지점별 세미프라임의 갯수를 구한다.
    semi_prime_cnt = [0] * (N + 1)
    for i in range(1, len(semi_prime_idx)):
        if semi_prime_idx[i]:
            semi_prime_cnt[i] = semi_prime_cnt[i - 1] + 1
        else:
            semi_prime_cnt[i] = semi_prime_cnt[i - 1]

    # 결과 리턴
    M = len(P)
    result = [0] * M

    for i in range(M):
        result[i] = semi_prime_cnt[Q[i]] - semi_prime_cnt[P[i] - 1]

    return result