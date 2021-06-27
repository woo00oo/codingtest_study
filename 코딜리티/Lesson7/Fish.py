def solution(A, B):
    stack = []

    for i in range(len(A)):
        if len(stack) == 0:
            stack.append((A[i], B[i]))
        # 스택의 맨 위 물고기가 상류로 흐르고 있다면 append
        elif stack[-1][1] == 0:
            stack.append((A[i], B[i]))
        else:
            # 스택의 맨 위 물고기가 하류로 흐르고 있고 새로들어올 물고기도 하류로 흐르고 있다면 append
            if B[i] == 1:
                stack.append((A[i], B[i]))
            # 스택의 맨 위 물고기가 하류로 흐르고 있고 새로들어올 물고기는 상류로 흐르고 있다면 더 큰 물고기로 change
            else:
                check = False
                for x in range(len(stack)-1, -1, -1):
                    if stack[x][1] == 1 and A[i] > stack[x][0]:
                        stack.pop()
                        check = True
                    elif stack[x][1] == 1 and A[i] < stack[x][0]:
                        check = False
                        break
                    else:
                        break
                if check:
                    stack.append((A[i], B[i]))

    return len(stack)