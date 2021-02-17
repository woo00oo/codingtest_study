# 2차원 배열의 맨 왼쪽 위부터 배열을 비교하며 값이 다를경우 3*3으로 값을 변환해 간다.

N, M = map(int, input().split())
matrix = [list(map(int,input())) for _ in range(N)]
matrix2 = [list(map(int,input())) for _ in range(N)]
answer = 0

for i in range(0, N-2):
    for j in range(0, M-2):
        if matrix[i][j] != matrix2[i][j]:
            answer += 1
            for row in range(3):
                for col in range(3):
                    if matrix[i+row][j+col] == 0:
                        matrix[i+row][j+col] = 1
                    else:
                        matrix[i+row][j+col] = 0

if matrix == matrix2:
    print(answer)
else:
    print(-1)
