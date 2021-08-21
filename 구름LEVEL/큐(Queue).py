N = int(input())
queue = list()

for _ in range(N):
    op = input()

    if op == 'd' or op == 'D':
        if len(queue) == 0:
            print("underflow")
        else:
            queue.pop(0)

    elif op == 'e' or op == 'E':
        num = int(input())

        if len(queue) == 10:
            print("overflow")
        else:
            queue.append(num)

    else:
        print(*queue)
        exit(0)

print(*queue)