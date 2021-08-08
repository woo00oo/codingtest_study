import sys
from itertools import permutations

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().split()))
operation = list(map(int, sys.stdin.readline().split()))

op = ['+', '-', '*', '//']
op_arr = []

for i in range(4):
    for _ in range(operation[i]):
        op_arr.append(op[i])

permu = list(set(permutations(op_arr, N-1)))
answer= []
for i in range(len(permu)):
    num = numbers[0]
    for j in range(len(permu[i])):
        now_op = permu[i][j]
        if now_op == '+':
            num += numbers[j+1]
        elif now_op == '-':
            num -= numbers[j+1]
        elif now_op == '*':
            num *= numbers[j+1]
        else:
            if num < 0 and numbers[j+1] > 0:
                num *= -1
                num //= numbers[j+1]
                num *= -1
            else:
                num //= numbers[j+1]

    answer.append(num)

print(max(answer))
print(min(answer))
