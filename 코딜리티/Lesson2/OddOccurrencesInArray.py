from collections import Counter

def solution(A):
    cnt_arr = list(Counter(A).items())

    for i in range(len(cnt_arr)):
        if cnt_arr[i][1] % 2 != 0:
            return cnt_arr[i][0]



