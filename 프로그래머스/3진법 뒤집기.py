# n이 3 보다 작을 경우에는 3진법 뒤집기 한 후에도 원래 n이 return
# 3보다 클 경우에는 10진법 -> 3진법으로 바꾼후 그 수를 뒤집어 다시 10진법으로 구한 수를 return
# 문제에서 제시하는 조건대로 구현하기만 하면 된다.

def solution(n):
    if n < 3:
        return n
    n3 = ''
    while True:
        if n // 3 < 3:
            n3 += str(n % 3)
            n3 += str(n // 3)
            break
        n3 += str(n % 3)
        n //= 3
    n3_li = list(n3)
    answer = 0
    num = 0
    for i in range(len(n3_li)-1,-1,-1):
        answer += int(n3_li[i]) * (3**num)
        num += 1
    return answer

