# 첫번째 풀이 : 재귀 활용 -> 시간 초과
# 시간 복잡도 : O(2^2/n)


def fibo(n):
    if n == 0:
        global count0
        count0 += 1
        return 0
    elif n == 1:
        global count1
        count1 += 1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

T = int(input())
for _ in range(T):
    count0 = 0
    count1 = 0
    N = int(input())
    fibo(N)
    print(count0, count1)


# 두번째 풀이: dp 활용 (반복문)
# 시간 복잡도 O(N)

T = int(input())
for _ in range(T):
    N = int(input())
    if N == 0:
        print(1, 0)
        continue
    if N == 1:
        print(0, 1)
        continue
    dp = [(0, 0)] * (N + 1)
    dp[0] = (1,0)
    dp[1] = (0,1)
    for i in range(2, N+1):
        dp[i] = (dp[i-1][0] + dp[i-2][0],dp[i-1][1] + dp[i-2][1])

    count0, count1 = dp[N]

    print(count0, count1)

