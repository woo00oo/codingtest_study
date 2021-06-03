# 첫번째 시도 : 중복된 값을 고려하지 않음.

def distance(homes, stores):
    chicken_distance = 0
    for home in homes:
        dis = float('inf')
        best_store = 0
        for i in range(len(stores)):
            d = abs(home[0]-stores[i][1][0]) + abs(home[1]-stores[i][1][1])
            if dis > d:
                dis = d
                best_store = i

        chicken_distance += dis
        stores[best_store][0] += 1

    return chicken_distance


N, M = map(int, input().split())
myMap = [list(map(int, input().split())) for _ in range(N)]
homes = []
stores = []
answer = 0

for i in range(N):
    for j in range(N):
        if myMap[i][j] == 1:
            homes.append((i+1, j+1))
        elif myMap[i][j] == 2:
            stores.append([0, (i+1, j+1)])

answer = distance(homes, stores)
if M == len(stores):
    print(answer)
else:
    stores.sort(key=lambda x: x[0], reverse=True)
    new_stores = stores[:M]
    answer = distance(homes, new_stores)
    print(answer)


