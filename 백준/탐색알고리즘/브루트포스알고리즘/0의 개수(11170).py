T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    numbers = [str(i) for i in range(N,M+1)]
    cnt = 0
    for num in numbers:
        for i in range(len(num)):
            if num[i] == '0':
                cnt += 1
    print(cnt)
