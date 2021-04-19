# most_common() -> 데이터의 개수가 많은 순으로 정렬된 배열을 리턴 ( 개수가 같은 요소는 처음 발견 된 순서대로 정렬 )
# 문제에서 요구하는 조건들이 Counter 모듈 안에 most_common() 메소드로 모두 해결 가능

from collections import Counter

N, C = map(int, input().split())

numbers = list(map(int, input().split()))

numbers = Counter(numbers).most_common()

answer = []

for i in range(len(numbers)):

    answer += [numbers[i][0]] * numbers[i][1]

print(*answer)