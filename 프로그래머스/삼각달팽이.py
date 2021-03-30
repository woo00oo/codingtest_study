def solution(n):
    res = [[0] * n for _ in range(n)] #삼각 달팽이를 저장할 res
    answer = list()
    x, y = -1, 0 #인덱스에 접근하기 위한 변수
    num = 1 # res에 저장할 수

    # 이중 for문으로 한변을 지날때마다 n개 ~ 1개로 저장할 수가 적어지니 0 ~ n, i ~ n 까지의 이중 for문 작성.
    for i in range(n):
        for j in range(i,n):
            if i % 3 == 0: #down
                x += 1
            elif i % 3 == 1: #right
                y += 1
            elif i % 3 == 2: #up
                x -= 1
                y -= 1
            res[x][y] = num
            num += 1

    # 2중 for문으로 answer에 저장한 후 반환.
    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)

    return answer