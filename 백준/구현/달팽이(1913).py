N = int(input())
w = int(input())
li = [[0 for i in range(N)] for j in range(N)]
n = 1

x = y = N // 2
check = 2
li[x][y] = n
i = 0
j = 0
while li[0][0] != N ** 2:
    x -= 1
    for i in range(check):
        n += 1
        li[x][y + i] = n
        if n == w:
            ans = [x + 1, y + i + 1]
    y += i
    for i in range(1, check + 1):
        n += 1
        li[x + i][y] = n
        if n == w:
            ans = [x + i + 1, y + 1]
    x += i
    for i in range(1, check + 1):
        n += 1
        li[x][y - i] = n
        if n == w:
            ans = [x + 1, y - i + 1]
    y -= i
    for i in range(1, check + 1):
        n += 1
        li[x - i][y] = n
        if n == w:
            ans = [x - i + 1, y + 1]
    x -= i
    check += 2

for i in range(N):
    for j in range(N):
        print(li[i][j], end=' ')
    print()
print(*ans)