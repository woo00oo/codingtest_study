N = int(input())
li = sorted(list(map(int, input().split())))
p1 = 0
p2 = len(li) - 1
min_sum = li[p1] + li[p2]

while p2 > p1:
    p1 += 1
    p2 -= 1
    if min_sum > li[p1] + li[p2]:
        min_sum = li[p1] + li[p2]

print(min_sum)