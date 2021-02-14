# 조합 공식 이용 : mCn => m! // (m-n)! * n!

import math

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(bridge)