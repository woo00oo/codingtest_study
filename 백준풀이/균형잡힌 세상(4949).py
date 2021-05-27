# 스택 자료 구조 활용.

while True:
    stack = []
    check = True
    S = input()

    if S == '.':
        exit(0)

    for i in range(len(S)):
        if S[i] == '(' or S[i] == '[':
            stack.append(S[i])
        elif S[i] == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                check = False
                break
        elif S[i] == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                check = False
                break

    if check:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')