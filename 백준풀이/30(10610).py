# 1차시도 : 메모리 초과
# N이 10^5개의 숫자임

from itertools import permutations

numbers = list(input())

permu = list(permutations(numbers, len(numbers)))
answer = -1

for i in range(len(permu)):
    num = int(''.join(permu[i]))
    if num % 30 == 0:
        if num > answer:
            answer = num

print(answer)

#30의 배수가 되는 조건
# - 일의 자리수가 0이여야 함.
# - 각 자리의 숫자들을 더했을 때 3으로 나누어 떨어져야함.

numbers = list(input())
numbers.sort(reverse=True)
sum = 0

for num in numbers:
    sum += int(num)

if sum % 3 != 0 or "0" not in numbers:
    print(-1)
else:
    print(''.join(numbers))

