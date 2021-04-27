# 조건 연산자 잘 확인하기 이하인지, 미만인지 잘 구별

apple = []
direction = []
time = 0
head = (1, 1)
snake = []
snake.append(head)
dx = [0, +1, 0, -1]
dy = [+1, 0, -1, 0]
index = 0

N = int(input())
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    apple.append((x, y))
L = int(input())
for _ in range(L):
    t, d = input().split()
    direction.append((int(t), d))
while True:
    for i in range(len(direction)):
        if time == direction[i][0]:
            if direction[i][1] == 'L':
                index -= 1
                if index < 0:
                    index = 3
            else:
                index += 1
            del direction[i]
            break

    head = ((head[0] + dx[index % 4]), (head[1] + dy[index % 4]))

    time += 1

    if not 0 < head[0] <= N or not 0 < head[1] <= N:
        print(time)
        break

    if head in snake:
        print(time)
        break

    snake.append(head)

    if head in apple:
        apple.remove(head)
    else:
        snake.pop(0)

