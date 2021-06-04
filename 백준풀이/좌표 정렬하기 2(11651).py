N = int(input())
location = []
for _ in range(N):
    x, y = map(int, input().split())
    location.append((x, y))

location.sort(key=lambda x:(x[1], x[0]))

for p in location:
    print(*p)
