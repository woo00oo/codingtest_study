# 쉬운 문제여도 문제에서 요구하는 조건들을 꼼꼼하게 파악하며 코딩 작성.
# 라이브 코딩에서는 이런 세심한 부분도 다 평가 되기 때문에 문제에서 요구하는 조건들을 꼼꼼히 파악하고, 만약 모호하다면 면접관에게 요구사항 제시 후 정확하게 해결.

from collections import Counter

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

# 산술 평균
print('%.f' % (sum(numbers) / N))

# 중앙값
numbers.sort()
print(numbers[N//2])

# 최빈값
count_numbers = list(Counter(numbers).items())
count_numbers.sort(key=lambda x: (x[1], -x[0]))
if len(count_numbers) > 1 and count_numbers[-1][1] == count_numbers[-2][1]:
    print(count_numbers[-2][0])
else:
    print(count_numbers[-1][0])

# 범위
print(numbers[-1] - numbers[0])