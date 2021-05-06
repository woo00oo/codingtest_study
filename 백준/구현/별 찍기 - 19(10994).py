# n에 따라서 (4*n-3) 만큼의 칸수들이 생기며 테두리를 감싸고 있는 것들의 내부에는 똑같은 것들이 반복.
# 따라서 재귀로 n을 1씩 줄이면서 x,y좌표의 값들을 2씩 더해준 후 재귀함수로 풀이.

def draw(n, idx):
    if n == 1:
        startMap[idx][idx] = '*'
        return
    l = 4 * n - 3

    for i in range(idx, l+idx):
        # 위 아래
        startMap[idx][i] = '*'
        startMap[idx+l-1][i] = '*'

        # 양 옆
        startMap[i][idx] = '*'
        startMap[i][idx+l-1] = '*'

    return draw(n-1, idx+2)



n = int(input())
lens = 4 * n - 3

startMap = [[' '] * lens for _ in range(lens)]

draw(n, 0)

for i in range(lens):
    for j in range(lens):
        print(startMap[i][j], end='')
    print()