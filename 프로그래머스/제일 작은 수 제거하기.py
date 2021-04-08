def solution(arr):
    if len(arr) <= 1:
        return -1
    else:
        Min = min(arr)
        arr.remove(Min)
        return arr