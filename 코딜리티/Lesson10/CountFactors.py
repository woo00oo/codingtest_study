# i * i <= n을 이용하면 sqrt(n)만에 풀 수 있다.
# i * i 다음에 등장하는 수는 앞에 이미 등장한 수와의 곱으로 표현하기 때문에 i*i까지만 조회하면 된다.

import math

def solution(N):
    answer = 0

    for i in range(1, int(math.sqrt(N) + 1)):
        if N % i == 0:
            if i * i == N:
                answer += 1
                break
            else:
                answer += 2

    return answer
