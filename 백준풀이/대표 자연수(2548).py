# 첫번째 시도 : 시간복잡도 O(N^2)

N = int(input())
numbers = list(map(int, input().split()))
answer = []


for i in range(N):
    S = 0
    for j in range(N):
        S += abs(numbers[i] - numbers[j])
    answer.append((numbers[i], S))

print(min(answer, key=lambda x: (x[1], x[0]))[0])

# 중앙값을 이용한 풀이
N = int(input())
numbers = sorted(list(map(int, input().split())))
q, r = divmod(N, 2)
print(numbers[q+r-1])
