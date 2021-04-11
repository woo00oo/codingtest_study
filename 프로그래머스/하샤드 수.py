def solution(x):
    li = list(map(int,str(x)))
    k = sum(li)
    if x % k == 0:
        return True
    else:
        return False