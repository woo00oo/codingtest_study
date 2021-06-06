# 시간 초과 : 반복문을 사용하지 않고 한번에 값을 계산해야 함.

A, B, V = map(int, input().split())
floor = 0
day = 0
while True:
    day += 1
    floor += A
    if floor >= V:
        print(day)
        break
    floor -= B

# -------------------

import math

A, B, V = map(int, input().split())
day = (V-B) / (A - B)
print(math.ceil(day))