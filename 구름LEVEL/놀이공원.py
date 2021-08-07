T = int(input())

for _ in range(T):

    N, K = map(int, input().split())
    my_map = [list(map(int, input().split())) for _ in range(N)]
    answer = K * K

    for i in range(0, N-K+1):
        for j in range(0, N-K+1):
            cnt = 0

            for x in range(i, i+K):
                for y in range(j, j+K):
                    if my_map[x][y] == 1:
                        cnt += 1

            if answer > cnt:
                answer = cnt

    print(answer)