N, K = map(int, input().split())

numbers = [i for i in range(1, N+1)]
kill = 0
while len(numbers) != 2:
    numbers.pop(kill)
    kill = (kill-1 + K) % len(numbers)

print(*numbers)