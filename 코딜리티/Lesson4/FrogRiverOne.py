def solution(X, A):

    numbers = {i for i in range(1, X+1)}

    for i in range(len(A)):
        if A[i] in numbers:
            numbers.remove(A[i])
        if len(numbers) == 0:
            return i

    return -1