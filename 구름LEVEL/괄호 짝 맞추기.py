S = input()
stack = []

for i in range(len(S)):
    if S[i] in ['(', '{', '[']:
        stack.append(S[i])
    else:
        if len(stack) == 0:
            print(False)
            exit(0)
        else:
            if S[i] == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    print(False)
                    exit(0)
            elif S[i] == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    print(False)
                    exit(0)
            else:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    print(False)
                    exit(0)

if len(stack) == 0:
    print(True)
else:
    print(False)
