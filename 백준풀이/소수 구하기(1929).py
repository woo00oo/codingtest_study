# 문제 해결:
#   에라토스테네스의 체

M, N = map(int, input().split())

numbers = [False, False] + [True] * (N-1)


for i in range(2, N+1):
    if numbers[i]:
        if i >= M:
            print(i)
        for j in range(2*i, N+1, i):
            numbers[j] = False



