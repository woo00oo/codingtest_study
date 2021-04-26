n, w, L = map(int,input().split())
truck = list(map(int,input().split()))
time = 0
queue = [0] * w

while queue:
    time += 1
    queue.pop(0)

    if truck:
        if sum(queue) + truck[0] <= L:
            queue.append(truck.pop(0))
        else:
            queue.append(0)

print(time)