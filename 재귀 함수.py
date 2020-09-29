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
