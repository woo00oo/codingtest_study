# 순열 활용

from itertools import permutations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sequence = list(permutations(numbers, M))
sequence.sort()

for i in range(len(sequence)):
    print(*sequence[i])