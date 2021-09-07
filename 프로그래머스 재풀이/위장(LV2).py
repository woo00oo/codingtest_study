def solution(clothes):
    items = dict()

    for i in range(len(clothes)):
        if clothes[i][1] in items:
            items[clothes[i][1]] += 1
        else:
            items[clothes[i][1]] = 1

    items_li = list(items.values())
    answer = 1

    for i in range(len(items_li)):
        answer *= items_li[i] + 1

    return answer - 1