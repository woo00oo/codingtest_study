# 문제풀이:
#   스택 자료구조를 활용하여 해결.
#   스택의 제일 위의 값과 넣을 값을 비교하며 넣을 값이 클 경우 스택의 제일 위의 값을 제거.
#

N, K = map(int,input().split())
number = list(map(int,input()))

stack = list()
del_num = K

for i in range(N):
    while del_num > 0 and stack:
        if stack[-1] < number[i]:
            stack.pop()
            del_num -= 1
        else:
            break
    stack.append(number[i])

for i in range(len(N-K)):
    print(stack[i], end='')