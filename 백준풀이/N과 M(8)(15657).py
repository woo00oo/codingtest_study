# 중복 조합 활용.

from itertools import combinations_with_replacement

N, M = map(int, input().split())
sequence = list(map(int, input().split()))
numbers = list(combinations_with_replacement(sequence, M))

for i in range(len(numbers)):
    numbers[i] = list(numbers[i])
    numbers[i].sort()

numbers.sort()

for num in numbers:
    print(*num)
