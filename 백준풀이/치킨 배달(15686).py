# 귀찮더라도 예제 입력을 모두 확인해보면 고려하지 못했던 힌트를 얻어 시간을 단축 시킬 수 있으니 예제 입력을 모두 확인해보는 습관을 가지자!!

from itertools import combinations

def distance(homes, stores):
    chicken_distance = 0
    for home in homes:
        dis = float('inf')
        for i in range(len(stores)):
            d = abs(home[0]-stores[i][0]) + abs(home[1]-stores[i][1])
            if dis > d:
                dis = d

        chicken_distance += dis

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
            stores.append((i+1, j+1))

if M == len(stores):
    print(distance(homes, stores))
else:
    new_stores = list(combinations(stores, M))
    answer = float('inf')
    for i in range(len(new_stores)):
        dis = distance(homes, new_stores[i])
        if answer > dis:
            answer = dis
    print(answer)


