li = list(map(int, input().split()))
goal = [1, 2, 3, 4, 5]

while li != goal:

    for i in range(len(li) - 1):

        if li[i] > li[i + 1]:
            li[i], li[i + 1] = li[i + 1], li[i]
            print(*li)