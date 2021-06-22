numbers = [0]

for i in range(1, 1001):
    if len(numbers) == 1001:
        break
    for j in range(i):
        numbers.append(i)
A, B = map(int, input().split())

print(sum(numbers[A:B+1]))