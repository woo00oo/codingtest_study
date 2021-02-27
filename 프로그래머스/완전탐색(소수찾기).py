from itertools import permutations


def check(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    li_numbers = list(numbers)
    sosu_list = list()
    for i in range(1, len(numbers) + 1):
        li = permutations(li_numbers, i)
        for number in li:
            num = ''
            for n in number:
                num += n
            num = int(num)
            if check(num) and num not in sosu_list:
                sosu_list.append(num)

    return len(sosu_list)


