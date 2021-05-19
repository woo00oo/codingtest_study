# 첫번째 시도 :
# 시간 복잡도 O(N*M) => 시간 초과.

import sys

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(sum(numbers[i-1:j]))

# 2번째 시도 :
#   누적합을 이용하여 O(N)으로 해결

import sys

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sum_li = [0]
sum_number = 0
for i in range(N):
    sum_number += numbers[i]
    sum_li.append(sum_number)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(sum_li[j] - sum_li[i-1])