# 스택 자료 구조를 활용.

def solution(s):
    stack = list()
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False