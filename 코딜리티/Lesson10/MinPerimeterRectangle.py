import math

def solution(N):
    answer = (1 + N) * 2

    for num in range(1, int(math.sqrt(N) + 1)):
        if N % num == 0:
            if (num + (N // num)) * 2 < answer:
                answer = (num + (N // num)) * 2

    return answer