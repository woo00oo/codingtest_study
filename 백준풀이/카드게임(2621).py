# 색깔의 개수, 숫자의 개수를 따로 저장하여 조건을 분리.

import sys
input = sys.stdin.readline

def solve():
    # 1
    if 5 in color_count.values():
        count = 0
        max_num = 0

        for number, cnt in enumerate(number_count):

            if cnt > 0:
                count += 1
                max_num = max(max_num, number)
            else:
                count = 0
            if count == 5:
                break

        if count == 5:

            result = max_num + 900
            return result
    # 2
    elif 4 in number_count:
        number = number_count.index(4)
        result = 800 + number
        return result
    # 3
    elif 3 in number_count and 2 in number_count:
        number3 = number_count.index(3)
        number2 = number_count.index(2)
        result = number3 * 10 + number2 + 700
        return result

    # 4
    if 5 in color_count.values():
        max_num = 0
        for color, number in card_list:
            if max_num < number:
                max_num = number
        result = 600 + number
        return result

    # 5
    cnt = 0
    max_num = 0
    for number, count in enumerate(number_count):
        if count > 0:
            cnt += 1
            max_num = max(max_num, number)
        else:
            cnt = 0
        if cnt == 5:
            break
    if cnt == 5:
        result = 500 + max_num
        return result
    # 6
    if 3 in number_count:
        number = number_count.index(3)
        result = 400 + number
        return result

    # 7
    cnt = 0
    max_num = 0
    min_num = 9
    for number, count in enumerate(number_count):
        if count == 2:
            cnt += 1
            max_num = max(max_num, number)
            min_num = min(min_num, number)
        if cnt == 2:
            break

    if cnt == 2:
        result = 10 * max_num + min_num + 300
        return result
    # 8
    if 2 in number_count:
        number = number_count.index(2)
        result = 200 + number
        return result
    # 9
    max_num = 0
    for color, number in card_list:
        if max_num < number:
            max_num = number

    return 100 + max_num

card_list = []
color_count = {
    'R':0,
    'B':0,
    'Y':0,
    'G':0,
}
number_count = [0] * 10

for _ in range(5):
    color, number = map(str, input().split())
    number = int(number)
    card_list.append((color, number))

    color_count[color] += 1
    number_count[number] += 1

card_list = sorted(card_list, key=lambda x: x[1])

answer = solve()
print(answer)