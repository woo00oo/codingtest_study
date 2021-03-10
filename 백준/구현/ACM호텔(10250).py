# 문제풀이:
#   간단한 2차원 배열 문제
#   실수 : 2차원 배열의 시작부분이 잘못 되었다 . 꼼꼼하게 볼것.

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    Y, X = 0, 0

    for j in range(W):

        for i in range(H-1,-1,-1):
            N -= 1
            if N == 0:
                X = j + 1
                Y = H - i
                if X < 10:
                    X = '0' + str(X)
                else:
                    X = str(X)
                Y = str(Y)
                print(Y + X)
                break
        if N == 0:
            break

