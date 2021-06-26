def solution(A):
    set_A = set(A)

    for i in range(1, len(A)+2):
        if i not in set_A:
            return i