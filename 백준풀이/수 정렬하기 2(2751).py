# 파이썬에서 sort() 메소드는 O(NlogN)의 시간복잡도를 가지고 있음

import sys

N = int(input())
numbers = []
for _ in range(N):
	numbers.append(int(sys.stdin.readline().strip()))

numbers.sort()

for i in range(N):
	print(numbers[i])