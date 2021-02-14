# 조합 공식 이용 : mCn => m! // (m-n)! * n!
# M개 중에서 N개를 선택한 후 차례대로 N개의 왼쪽 사이트에 순서대로 맞춰주기만 하면 됨

import math

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(bridge)