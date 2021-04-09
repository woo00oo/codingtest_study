def solution(s):
    numbers = s.split(' ')

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    # numbers = list(map(int,numbers)) => 리스트의 각 원소를 int형으로 변경
    Max = max(numbers)
    Min = min(numbers)

    return str(Min) + ' ' + str(Max)