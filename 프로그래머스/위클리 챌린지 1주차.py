def solution(price, money, count):
    total = 0

    for i in range(1, count+1):
        total += price * i

    money -= total

    if money < 0:
        return abs(money)
    else:
        return 0

