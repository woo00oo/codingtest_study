N = int(input())
paper = [[0] * 101 for _ in range(101)]
area = 0

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            paper[i][j] = 1

for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            area += 1

print(area)