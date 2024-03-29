# 가로가 8, 세로가 12일 경우
# 대각선은 (0,0) 과 (8,12)를 지나고, 직선의 식은 y = 2/3x와 같음
# 즉, x가 2의 배수일 때, y가 3의 배수일 때 점을 지난다
# 이 때 직선이 지나가는 점의 개수는 4개이다 즉, 8과 12의 최대 공약수


import math

def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))