N = int(input())
location = []
for _ in range(N):
    x, y = map(int, input().split())
    location.append((x, y))

location.sort()

for i in range(N):
    print(*location[i])
