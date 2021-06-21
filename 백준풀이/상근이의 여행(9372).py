# 애초에 모든 국가가 연결되어 있기 때문에 비행기 종류의 최소 개수는 국가 수 -1 이다.

import sys
T = int(sys.stdin.readline())

for i in range(T):

    N, M = map(int, sys.stdin.readline().split())

    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())

    print(N - 1)