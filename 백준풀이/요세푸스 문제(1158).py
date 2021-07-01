# N명의 사람들이 있고, K를 주기로 사람들을 제거하는 문제.
# K(주기)가 사람의 전체 인원수를 초과하면 사람의 인원수로 나눈 나머지로 값을 초기화.

N, K = map(int, input().split())

numbers = [i for i in range(1, N+1)]
answer = []
num = 0

for i in range(N):
    num += K - 1
    if num >= len(numbers):
        num %= len(numbers)

    answer.append(str(numbers.pop(num)))

print("<", ", ".join(answer), ">", sep='')