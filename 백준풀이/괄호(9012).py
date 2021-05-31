N = int(input())

for _ in range(N):
    s = input()
    stack = []
    VPS = True
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) == 0:
                VPS = False
            else:
                stack.pop()
    if len(stack) != 0:
        VPS = False

    if VPS:
        print("YES")
    else:
        print("NO")