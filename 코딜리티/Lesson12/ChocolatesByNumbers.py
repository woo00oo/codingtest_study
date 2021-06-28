from math import gcd

def solution(N, M):
    return N // gcd(N, M)