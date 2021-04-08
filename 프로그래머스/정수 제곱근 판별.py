import math

def solution(n):
    answer = math.sqrt(n)
    if answer == int(answer):
        return (answer + 1)**2
    else:
        return -1
