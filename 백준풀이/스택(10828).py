import sys

N = int(input())
stack = []

for _ in range(N):
    command = sys.stdin.readline().strip()

    if "push " in command:
        command = command.replace("push ", '')
        stack.append(int(command))

    elif command == "pop":
        try:
            numbers = stack.pop()
            print(numbers)
        except:
            print(-1)

    elif command == "size":
        print(len(stack))

    elif command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif command == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)