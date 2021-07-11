# 1차 시도 : 시간 초과
#   insert 메서드 때문에 시간초과가 난 듯 싶다.

import sys

S = list(' ' + input())
cursor = len(S) - 1
M = int(input())

for _ in range(M):
    op = sys.stdin.readline().strip()

    if op == 'L':
        if cursor != 0:
            cursor -= 1

    elif op == 'D':
        if cursor != len(S) - 1:
            cursor += 1

    elif op == 'B':
        if cursor != 0:
            del S[cursor]
            cursor -= 1

    elif 'P' in op:
        op = op.replace('P ', '')
        S.insert(cursor+1, op)
        cursor += 1

answer = S[1:]
print(''.join(answer))


# 2차 시도 :
#   insert는 O(N)의 시간 복잡도를 가지기 때문에 이를 스택 2개를 활용하여 O(1)로 줄일 수 있다.
from sys import stdin

stack1 = list(stdin.readline().strip())
stack2 = []
N = int(input())
for line in stdin:
    if line[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
        else:
            continue
    elif line[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
        else:
            continue
    elif line[0] == 'B':
        if stack1:
            stack1.pop()
        else:
            continue
    elif line[0] == 'P':
        stack1.append(line[2])

print(''.join(stack1 + list(reversed(stack2))))