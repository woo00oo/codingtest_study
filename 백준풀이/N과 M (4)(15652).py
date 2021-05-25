# 중복 순열을 활용하여 풀이.

from itertools import combinations_with_replacement

N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
sequence = list(combinations_with_replacement(numbers, M))
sequence.sort()

for i in range(len(sequence)):
    print(*sequence[i])