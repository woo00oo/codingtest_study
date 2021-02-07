N = int(input())
li = list()
for _ in range(N):
    x, y = map(int, input().split())
    li.append((x, y))
for i in li:
    grade = 0
    for j in li:
        if i != j and i[0] < j[0] and i[1] < j[1]:
            grade += 1
    print(grade+1, end=' ')
