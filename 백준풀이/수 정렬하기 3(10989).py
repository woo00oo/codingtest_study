# O(N)으로 해결.
import sys

N = int(input())
numbers = dict()
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num in numbers:
        numbers[num] += 1
    else:
        numbers[num] = 1

for num in range(100001):
    if num in numbers:
        for i in range(numbers[num]):
            print(num)

#  ---------------

import sys

N = int(sys.stdin.readline())
numbers = [0] * 10001

for i in range(N):
    numbers[int(sys.stdin.readline())] += 1

for i in range(10001):
    if numbers[i] != 0:
        for j in range(numbers[i]):
            print(i)