from collections import deque

A, B = map(int, input().split())
m = int(input())
numbers = list(map(int, input().split()))

# A진법 -> 10진법
number_10 = 0
i = 0
for num in range(m-1, -1, -1):
    number_10 += numbers[num] * (A ** i)
    i += 1

answer = deque()
# 10진법 -> B진법
while True:
    answer.appendleft(number_10 % B)
    number_10 //= B
    if number_10 < B:
        answer.appendleft(number_10)
        break

print(*answer)

