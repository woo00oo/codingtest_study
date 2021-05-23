# 조합

from itertools import combinations

N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]

arr = list(combinations(numbers, M))
arr.sort()

for i in range(len(arr)):
    print(*arr[i])

