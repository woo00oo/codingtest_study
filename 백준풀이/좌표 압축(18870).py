# set 자료구조를 사용하여 중복을 없앨 수 있다.

N = int(input())
numbers = list(map(int, input().split()))
sort_numbers = sorted(set(numbers))
answer = {value: index for index, value in enumerate(sort_numbers)}

for key in numbers:
    print(answer[key], end=' ')

