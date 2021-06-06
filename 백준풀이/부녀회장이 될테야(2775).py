T = int(input())


for _ in range(T):
    k = int(input())
    n = int(input())
    layer = [[i for i in range(n+1)] for _ in range(k+1)]

    for i in range(1, len(layer)):
        for j in range(1, len(layer[i])):
            layer[i][j] = sum(layer[i-1][:j+1])

    print(layer[k][n])