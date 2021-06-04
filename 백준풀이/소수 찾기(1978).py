N = int(input())
numbers = list(map(int, input().split()))
decimal = [True] * 1001
decimal[1] = False

for i in range(2, 1001):
    if decimal[i]:
        for num in range(i*2, 1001, i):
            decimal[num] = False
answer = 0
for num in numbers:
    if decimal[num]:
        answer += 1

print(answer)
