# 유클리드 호제법을 이용한 최대 공약수, 최소 공배수 구하기
# 최소 공배수 = a * b / 최대 공약수

def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a


def solution(n, m):
    return [gcd(n, m), n * m / gcd(n, m)]


# import math 라이브러리 활용
# math.gcd -> 최대 공약수를 구해주는 메소드