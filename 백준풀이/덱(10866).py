from collections import deque
import sys

N = int(input())
deq = deque()

for _ in range(N):
    command = sys.stdin.readline().strip()

    if "push_front" in command:
        command = command.replace("push_front ", '')
        deq.appendleft(int(command))
    elif "push_back" in command:
        command = command.replace("push_back ", '')
        deq.append(int(command))
    elif command == 'pop_front':
        try:
            value = deq.popleft()
            print(value)
        except:
            print(-1)
    elif command == 'pop_back':
        try:
            value = deq.pop()
            print(value)
        except:
            print(-1)
    elif command == 'size':
        print(len(deq))
    elif command == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        try:
            print(deq[0])
        except:
            print(-1)
    else:
        try:
            print(deq[-1])
        except:
            print(-1)