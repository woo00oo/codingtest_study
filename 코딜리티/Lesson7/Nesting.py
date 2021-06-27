# 리스트의 인덱스를 접근할 때 항상 그 리스트의 사이즈가 어떻게 되는지 체크한다. (빈 리스트일 경우 에러가 날 수 있음)

def solution(S):
    stack = []

    for i in range(len(S)):
        if S[i] == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                return 0
        else:
            stack.append(S[i])

    if len(stack) == 0:
        return 1
    else:
        return 0