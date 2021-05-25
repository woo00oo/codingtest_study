import sys
from collections import deque

N = int(input())
queue = deque()

for _ in range(N):
    command = sys.stdin.readline().strip()

    if "push " in command:
        command = command.replace("push ", '')
        queue.append(int(command))

    elif command == "pop":
        try:
            numbers = queue.popleft()
            print(numbers)
        except:
            print(-1)

    elif command == "size":
        print(len(queue))

    elif command == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif command == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)

    elif command == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)