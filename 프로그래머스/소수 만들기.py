from itertools import combinations

def solution(nums):
    cnt = 0
    li = list(combinations(nums,3))
    for i in range(len(li)):
        if check(sum(li[i])):
            cnt += 1
    return cnt

def check(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True