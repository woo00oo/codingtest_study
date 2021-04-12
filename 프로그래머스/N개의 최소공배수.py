# 최소공배수를 누적하여 구해준다.
# math.gcd => 최대 공약수를 구해주는 라이브러리.

import math

def solution(arr):
    answer = arr[0]
    for num in arr:
        answer = num * answer / math.gcd(num, answer)
    return answer
