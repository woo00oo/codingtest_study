# 첫번째 시도 : 브루트 포스 알고리즘으로 해결 => 시간초과
# 단순 M,N이 40,000이라 O(N)의 시간복잡도로 해결할 수 있을거라 생각하였지만 조건에 따라 1로 초기화가 때문에 40,000보다 훨씬 큰 수가 N,M으로 잡힘
# => N의 범위를 정확히 파악한 후 로직을 설계하자.

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())

    answer = 1
    cx, cy = 1, 1
    check = False
    while True:

        if cx == M and cy == N:
            break

        if cx == x and cy == y:
            print(answer)
            check = True
            break

        if cx < M:
            cx += 1
        else:
            cx = 1

        if cy < N:
            cy += 1
        else:
            cy = 1

        answer += 1

    if not check:
        print(-1)

# 2번째 시도: 간단한 규칙을 찾아서 해결해야하는 문제
# k번째 해 즉, 정답이 k라고 가정하면 k - x에 m을 나누면 나머지가 0 이다. 마찬가지로 k - y에 n을 나누면 나머지가 0 이다.
# 정답 : k는 x나 y에 m과 n을 계속 더한 값중 하나.
# x에 m을 게속 더해주고 y를 뺀 값에 n이 나누어 떨어진다면 그 값이 정답이다.

def num(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(num(M, N, x, y))