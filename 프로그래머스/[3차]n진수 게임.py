# 10진수 -> n진수 변환
def trans(n, num):
    arr = "0123456789ABCDEF"
    ret = ''

    if num == 0:
        return '0'

    while num > 0:
        ret = arr[num % n] + ret
        num //= n

    return ret


def solution(n, t, m, p):
    answer = ''
    numbers = ''

    # 0부터 t * m 까지의 숫자 나열(10진수 -> n진수로 변환)
    for i in range(t * m):
        numbers += trans(n, i)

    for s in range(p - 1, t * m, m):
        answer += numbers[s]

    return answer