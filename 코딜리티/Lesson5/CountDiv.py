# 경계 값 예외 처리를 잘 생각하자

def solution(A, B, K):

    if A % K == 0:
        return B // K - A // K + 1

    else:
        return B // K - A // K