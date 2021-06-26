def solution(A):
    numbers = set(A)
    if len(numbers) != len(A):
        return 0

    for i in range(1, len(numbers)+1):
        if i not in numbers:
            return 0

    return 1