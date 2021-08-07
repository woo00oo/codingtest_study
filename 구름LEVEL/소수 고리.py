from itertools import permutations
from math import sqrt


def sosu(num):
    cnt = 0

    for x in range(1, int(sqrt(num)) + 1):
        if num % x == 0:
            cnt += 1

    return cnt


def check(li):
    for idx in range(len(li)):

        if idx == len(li) - 1:
            num = li[idx] + li[0]
            cnt = sosu(num)
        else:
            num = li[idx] + li[idx+1]
            cnt = sosu(num)

        if cnt != 1:
            return False

    return True


n = int(input())
arr = [i for i in range(2, n+1)]
answer = []

# 순열 생성
permu = list(permutations(arr, n-1))

for i in range(len(permu)):
    li = [1] + list(permu[i])

    # 소수 판별
    result = check(li)

    if result:
        answer.append(li)

for ans in answer:
    print(*ans)