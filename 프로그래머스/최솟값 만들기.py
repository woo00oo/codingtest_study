# 두배열에서 하나는 가장 작은 값, 하나는 가장 큰 값을 순차적으로 곱해서 더해주면 문제 해결 가능.

def solution(A, B):
    A = sorted(A, reverse = True)
    B = sorted(B)
    answer = 0

    for i, j in zip(A,B):
        answer += i * j

    return answer