#1부터 num까지의 곱을 출력해주는 함수
def multiple(num):
    if num <= 1:
        return num
    return num * multiple(num-1)

#리스트의 합을 리턴하는 함수
def sum_list(num):
    if len(num) <= 1:
        return num[0]
    return num[0] + sum_list(num[1:])

#회문을 판별할 수 있는 함수
def palindrome(data):
    # if data == data[::-1]:
    #     return True
    # return False
    if len(data) == 1:
        return True
    if data[0] == data[-1]:
        return palindrome(data[1:-1])
    else:
        return False
def func(n):
    print(n)
    if n == 1:
        return n

    if n%2 == 1:
        return (func(3 * n +1))
    else:
        return (int(func(n / 2)))

#재귀용법의 패턴을 찾자!
def sum(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4

    return sum(num-1) +sum(num-2) + sum(num -3)