while True:
    n = list(map(int, input().split()))
    if sum(n) == 0:
        exit(0)

    n.sort()
    if n[0] ** 2 + n[1] ** 2 == n[2] ** 2:
        print('right')
    else:
        print('wrong')