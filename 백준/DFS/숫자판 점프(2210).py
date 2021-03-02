# 왔던 길을 다시 돌아갈 수 있기에 중복 체크 코드를 넣어주지 않아도 된다.
# DFS는 스택이나 재귀함수를 통해서 구현할 수 있다.

def DFS(x,y,number):
    if len(number) == 6:
        if number not in answer:
            answer.add(number)
        return
    for i in range(4):
        ddx = x + dx[i]
        ddy = y + dy[i]

        if 0 <= ddx < 5 and 0 <= ddy < 5:
            DFS(ddx,ddy, number + board[ddx][ddy])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
board = [list(map(str,input().split())) for _ in range(5)]
answer = set()
for i in range(5):
    for j in range(5):
        DFS(i,j,board[i][j])

print(len(answer))